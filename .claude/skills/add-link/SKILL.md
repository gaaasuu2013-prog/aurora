---
name: add-link
description: ASPで発行した紹介リンク、または案件のID（Amazonのトラッキングタグ、GetYourGuideのpartner_idなど）を台帳 data/affiliates.md に登録する。
argument-hint: [案件名]
disable-model-invocation: true
---

案件：$ARGUMENTS

1. 運営者に、ASPの管理画面からコピーしたリンク（HTMLタグでも可）か、IDを貼ってもらう。
2. 案件名、ASP、リンクまたはID、**リンクの作り方**（そのまま使う／商品URLにIDを付けて作る、など案件の規約で認められた方法だけ）を `data/affiliates.md` の表に書く。作り方がわからなければ「そのまま使う」にする。
3. 独自ドメインへ移る前なら「公開可」は「まだ」のまま。移った後なら「はい」。
4. この案件が使えるバックログの記事を挙げて終える。
