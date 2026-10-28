---
name: monthly
description: 月報とバックログの見直し。毎月1日のスケジュール実行で使う。
disable-model-invocation: true
---

運営者はこの場にいない前提で進めてください。

1. **analyst** に先月の数字を取らせ、月報 `data/reports/monthly-YYYY-MM.md` を書かせる。
2. 月報をもとに `data/backlog.md` の優先度を並べ替え、新しい記事候補を最大6本足す（季節、検索語、体験メモの有無を考える）。
3. 表示が多いのにクリックが少ない記事があれば、タイトルと説明文の手直しを1件だけ行う（tier: auto の記事なら main へ、approve の記事ならプルリクエスト）。
4. **strategist** に月次の戦略見直しを頼む（`/plan` と同じ分析。方針の変更案があればプルリクエスト）。
5. main にコミットして push し、来月の重点3つと strategist の「次の一手」を表示する。
