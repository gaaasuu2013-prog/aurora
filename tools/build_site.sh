#!/bin/sh
# Cloudflare Pages 用：公開するファイルだけを dist/ に集める（content/ data/ tools/ などは出さない）
set -e
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
cp *.html *.js *.css *.png manifest.webmanifest sitemap.xml dist/
cp -r blog dist/
[ -f robots.txt ] && cp robots.txt dist/ || true
# 404.html があると、Cloudflare Pages は存在しないURLにトップページではなく 404 を返す
cat > dist/404.html <<'HTML'
<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>ページが見つかりません - 極光ナビ</title>
<link rel="stylesheet" href="/app.css"></head>
<body><main style="max-width:640px;margin:48px auto;padding:0 16px">
<h1>ページが見つかりません</h1>
<p>URLが変わったか、ページがなくなった可能性があります。</p>
<p><a href="/">極光ナビ（今夜のオーロラ予報）へ</a> ／ <a href="/blog/">旅ブログの記事一覧へ</a></p>
</main></body></html>
HTML
echo "dist/ に $(find dist -type f | wc -l) ファイル"
