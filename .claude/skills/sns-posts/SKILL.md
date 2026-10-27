---
name: sns-posts
description: 公開した記事から Instagram と X の投稿案を作る。
argument-hint: <記事のslug>
disable-model-invocation: true
---

記事：$ARGUMENTS

**sns-writer** に `content/blog/$ARGUMENTS.md` から投稿案を作ってもらい、`content/sns/$ARGUMENTS.md` に保存して、Instagram のキャプションと X の3本をそのまま貼れる形で表示してください。
