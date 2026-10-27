---
name: new-article
description: 新しいブログ記事を、調査→下書き→点検→仕上げ→プルリクエストまで通しで作る。
argument-hint: <記事のテーマ>
disable-model-invocation: true
---

テーマ：$ARGUMENTS

CLAUDE.md のルールに従い、次の順で進めてください。

1. テーマから英語の slug を決める（例：ry-rental-suitcase）。`content/blog/` に同じテーマの記事がないか確かめ、あれば新しく作らず、その記事の更新として進める。
2. **researcher** に調査を頼み、`content/research/<slug>.md` を作る。
3. `content/notes/` から、このテーマに関係する体験メモを探す。必要な体験が足りなければ、具体的な質問を `data/questions.md` に足し、その場で運営者に聞いてよいか尋ねる（その場で答えてもらえれば **interviewer** として聞き取る）。調査だけで書ける記事（柱D、または比較記事）は続けてよい。
4. **writer** に下書きを頼む。
5. **fact-checker** に点検を頼む。「不合格」なら writer に直させ、もう一度点検（最大2回）。
6. **reviewer** に採点を頼む。80点未満なら直して再採点（最大2回）。
7. **seo-editor** に仕上げとビルドと公開（区分どおり）を頼む。
8. 最後に、公開したURLまたはプルリクエストのURL、運営者が埋める空欄の一覧、点検の判定を短く報告する。
