#!/usr/bin/env python3
"""極光ナビ ブログのビルド。

content/blog/*.md（status: ready のものだけ）→ blog/<slug>.html と blog/index.html を作り、
sitemap.xml のブログ部分を書き直す。リポジトリのルートで `python3 tools/build_blog.py` を実行する。
`--check` をつけると、ファイルを書かずにチェックだけ行う（GitHub Actions 用）。
必要なもの：pip install markdown
"""
import html, json, re, sys, datetime, pathlib

try:
    import markdown
except ImportError:
    sys.exit("markdown が入っていません。先に `pip install markdown` を実行してください。")

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "content" / "blog"
OUT = ROOT / "blog"
SITEMAP = ROOT / "sitemap.xml"

# 独自ドメインへ移ったらここを書き換える（末尾の / を忘れずに）
SITE = "https://gaaasuu2013-prog.github.io/aurora/"
GOATCOUNTER = "https://gaaasuu2013.goatcounter.com/count"
SITE_NAME = "極光ナビ"

PLACES = {
    "rovaniemi": "ロヴァニエミ", "saariselka": "サーリセルカ", "helsinki": "ヘルシンキ",
    "tromso": "トロムソ", "abisko": "アビスコ", "reykjavik": "レイキャビク",
    "fairbanks": "フェアバンクス", "yellowknife": "イエローナイフ", "rikubetsu": "陸別",
}
PILLARS = {"A": "観測地ガイド", "B": "旅の準備", "C": "空港とラウンジ", "D": "オーロラの基礎"}
REQUIRED = ["title", "description", "slug", "date", "pillar", "status"]
PLACEHOLDER = re.compile(r"【(体験メモが必要|リンク未発行)[^】]*】")
AFFILIATE_HOSTS = re.compile(
    r"(a8\.net|valuecommerce|moshimo|afi-b|accesstrade|janet|amzn\.to|amazon\.co\.jp/[^\s)]*tag=|"
    r"hb\.afl\.rakuten|partner_id=|booking\.com/[^\s)]*aid=|awin1\.com)", re.I)
PR_NOTE = "本記事にはアフィリエイト広告（PR）を含みます。"


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("front matter（--- で囲んだ部分）がありません")
    meta = {}
    for line in m.group(1).splitlines():
        line = line.split("  #")[0].rstrip()
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def check(meta, body, name):
    errs = [f"{k} がありません" for k in REQUIRED if not meta.get(k)]
    if meta.get("pillar") and meta["pillar"] not in PILLARS:
        errs.append("pillar は A / B / C / D のどれか")
    if meta.get("tier", "approve") not in ("auto", "approve"):
        errs.append("tier は auto か approve")
    if meta.get("place") and meta["place"] not in PLACES:
        errs.append(f"place '{meta['place']}' はアプリのページIDにありません")
    if PLACEHOLDER.search(body):
        errs.append("【体験メモが必要】【リンク未発行】の空欄が残っています")
    has_aff = bool(AFFILIATE_HOSTS.search(body))
    is_aff = meta.get("affiliate", "false").lower() == "true"
    if has_aff and not is_aff:
        errs.append("紹介リンクがあるのに affiliate: true になっていません")
    if is_aff and "github.io" in SITE:
        errs.append("独自ドメインへ移るまで、紹介リンクつきの記事は公開できません")
    return [f"{name}: {e}" for e in errs]


CSS = """
:root{--night:#0a1122;--panel:#101a30;--line:#26334f;--snow:#e8edf5;--mute:#8f9cb5;--oxygen:#5ef0a6;--warn:#f2c14e;
--f-display:"Zen Old Mincho","Hiragino Mincho ProN","Yu Mincho",serif;--f-body:"Zen Kaku Gothic New","Hiragino Sans","Noto Sans JP",system-ui,sans-serif}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--night);color:var(--snow);font-family:var(--f-body);line-height:1.85;font-size:17px}
a{color:var(--oxygen)}
.wrap{max-width:720px;margin:0 auto;padding:0 16px 64px}
header.bar{border-bottom:1px solid var(--line);padding:12px 16px;display:flex;gap:16px;align-items:center;justify-content:space-between;max-width:720px;margin:0 auto}
header.bar a{color:var(--snow);text-decoration:none}
.brand{font-family:var(--f-display);font-weight:900;font-size:20px}
.crumb{font-size:13px;color:var(--mute);margin:20px 0 4px}
h1{font-family:var(--f-display);font-size:30px;line-height:1.4;margin:4px 0 12px}
h2{font-family:var(--f-display);font-size:23px;margin:44px 0 12px;padding-top:12px;border-top:1px solid var(--line)}
h3{font-size:19px;margin:28px 0 8px}
.meta{color:var(--mute);font-size:13px}
.pr{border:1px solid var(--line);border-radius:8px;padding:8px 12px;font-size:14px;color:var(--warn);margin:16px 0}
.cta{display:block;background:var(--panel);border:1px solid var(--oxygen);border-radius:12px;padding:14px 16px;margin:20px 0;text-decoration:none;color:var(--snow)}
.cta b{color:var(--oxygen)}
img{max-width:100%;height:auto;border-radius:8px}
table{border-collapse:collapse;width:100%;font-size:15px;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}
th{background:var(--panel)}
blockquote{margin:16px 0;padding:4px 16px;border-left:3px solid var(--oxygen);color:var(--mute)}
.list a{display:block;padding:14px 0;border-bottom:1px solid var(--line);text-decoration:none;color:var(--snow)}
.list .t{font-weight:700;font-size:18px}.list .d{color:var(--mute);font-size:14px}
footer{color:var(--mute);font-size:13px;border-top:1px solid var(--line);margin-top:48px;padding-top:16px}
"""


def page(title, desc, url, body, extra_head=""):
    return f"""<!doctype html>
<html lang="ja"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article"><meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#0a1122">
<link rel="icon" href="../favicon-32.png" sizes="32x32" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;700&family=Zen+Old+Mincho:wght@700;900&display=swap">
<style>{CSS}</style>
{extra_head}
<script data-goatcounter="{GOATCOUNTER}" async src="https://gc.zgo.at/count.js"></script>
</head><body>
<header class="bar"><a class="brand" href="../">極光ナビ</a><a href="./">旅ブログ</a></header>
<main class="wrap">{body}
<footer>極光ナビ 旅ブログ｜記事づくりにはAIを使い、体験の記述と最終確認は運営者が行っています。<br>
<a href="../">今夜のオーロラ予報を見る</a></footer>
</main></body></html>
"""


def build(check_only=False):
    posts, errors = [], []
    for path in sorted(SRC.glob("*.md")):
        if path.name.startswith("_"):
            continue
        try:
            meta, body = parse(path)
        except ValueError as e:
            errors.append(f"{path.name}: {e}")
            continue
        if meta.get("status") != "ready":
            print(f"skip（下書き）: {path.name}")
            continue
        errs = check(meta, body, path.name)
        if errs:
            errors += errs
            continue
        posts.append((meta, body))
    if errors:
        print("\n".join(["ビルドを止めました："] + ["  - " + e for e in errors]))
        sys.exit(1)
    if check_only:
        print(f"チェックOK：公開できる記事 {len(posts)} 本")
        return

    OUT.mkdir(exist_ok=True)
    posts.sort(key=lambda p: p[0].get("updated") or p[0]["date"], reverse=True)
    for meta, body in posts:
        slug = meta["slug"]
        url = f"{SITE}blog/{slug}.html"
        content = markdown.markdown(body, extensions=["tables", "toc", "sane_lists"])
        content = content.replace('<a href="http', '<a rel="noopener" target="_blank" href="http')
        top = ""
        if meta.get("affiliate", "").lower() == "true":
            top += f'<p class="pr">{PR_NOTE}</p>'
        if meta.get("place"):
            name = PLACES[meta["place"]]
            top += (f'<a class="cta" href="../{meta["place"]}.html"><b>今夜の{name}のオーロラ予報</b><br>'
                    f'見えやすさ・雲・ねらい目の時間を極光ナビで確認する →</a>')
        upd = meta.get("updated") or meta["date"]
        ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": meta["title"],
              "description": meta["description"], "datePublished": meta["date"], "dateModified": upd,
              "inLanguage": "ja", "mainEntityOfPage": url, "image": f"{SITE}og.png",
              "author": {"@type": "Organization", "name": SITE_NAME, "url": SITE},
              "publisher": {"@type": "Organization", "name": SITE_NAME, "url": SITE}}
        body_html = (f'<p class="crumb"><a href="./">旅ブログ</a> › {PILLARS[meta["pillar"]]}</p>'
                     f'<h1>{html.escape(meta["title"])}</h1>'
                     f'<p class="meta">公開 {meta["date"]}　更新 {upd}</p>{top}{content}')
        head = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
        (OUT / f"{slug}.html").write_text(
            page(f'{meta["title"]}｜{SITE_NAME}', meta["description"], url, body_html, head), encoding="utf-8")

    items = "".join(
        f'<a href="{m["slug"]}.html"><span class="t">{html.escape(m["title"])}</span><br>'
        f'<span class="d">{PILLARS[m["pillar"]]}・{m.get("updated") or m["date"]}｜{html.escape(m["description"])}</span></a>'
        for m, _ in posts) or "<p>記事を準備中です。</p>"
    idx = (f'<h1>極光ナビ 旅ブログ</h1><p class="meta">オーロラ旅の計画・準備・空港ラウンジの実録。</p>'
           f'<div class="list">{items}</div>')
    (OUT / "index.html").write_text(
        page(f"旅ブログ｜{SITE_NAME}", "オーロラ旅の観測地ガイド、持ち物、撮影、空港ラウンジの実録をまとめた極光ナビの旅ブログです。",
             f"{SITE}blog/", idx), encoding="utf-8")

    # 記事が消えた場合に古いHTMLを残さない
    keep = {f"{m['slug']}.html" for m, _ in posts} | {"index.html"}
    for f in OUT.glob("*.html"):
        if f.name not in keep:
            f.unlink()

    if SITEMAP.exists():
        sm = SITEMAP.read_text(encoding="utf-8")
        sm = re.sub(r"\s*<url>\s*<loc>[^<]*/blog/[^<]*</loc>.*?</url>", "", sm, flags=re.S)
        today = datetime.date.today().isoformat()
        add = f"  <url><loc>{SITE}blog/</loc><lastmod>{today}</lastmod></url>\n" + "".join(
            f"  <url><loc>{SITE}blog/{m['slug']}.html</loc><lastmod>{m.get('updated') or m['date']}</lastmod></url>\n"
            for m, _ in posts)
        sm = sm.replace("</urlset>", add + "</urlset>")
        SITEMAP.write_text(sm, encoding="utf-8")
    print(f"できました：記事 {len(posts)} 本 → blog/")


if __name__ == "__main__":
    build(check_only="--check" in sys.argv)
