---
name: factory
description: 記事工場を1回まわす。企画→調査→下書き→点検→採点→仕上げ→公開（自動 or 承認待ち）まで。スケジュール実行で週2回使う。
disable-model-invocation: true
---

CLAUDE.md と `data/config.md` を読んでから、次の順で進めてください。運営者はこの場にいない前提で、質問で止まらずに最後まで進めます。

1. `pip install markdown`（未導入なら）。
2. 今週（月曜始まり）すでに公開した本数を git log の「公開:」コミットから数える。`WEEKLY_LIMIT` に達していれば、手順3〜8は行わず手順9だけ行う。
3. **planner** に次の記事を選んでもらう。選べなければ手順9へ。
4. **researcher** が調査メモを作る。
5. **writer** が下書きを書く。
6. **fact-checker** が点検。「不合格」なら writer が直して再点検（最大2回）。それでも不合格なら、その記事は `data/backlog.md` で「要人間確認」にして手順9へ。
7. **reviewer** が採点。80点未満なら writer と seo-editor で直して再採点（最大2回）。80点に届かなければ tier を approve にする。
8. **seo-editor** が仕上げ、公開区分どおりに main へ push するか、プルリクエストを作る。SNS投稿案も作らせる。
9. `data/questions.md` の未回答の数を数える。
10. 最後に次の形で報告する（これが運営者への通知になる）。
```
今回：<記事タイトル>｜自動公開 / 承認待ち（PRのURL）/ 体験待ち
採点：nn点　点検：合格
運営者へのお願い：<なし、または「/trip-log で質問n個に答えてください」>
```
