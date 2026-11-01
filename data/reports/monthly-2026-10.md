# 月報 2026-10（作成 2026-11-01／analyst）

対象：2026-10-01〜10-31。
数字は git log・`content/`・`data/` から数えたものだけです。推測の数字は入れていません。

## 0. 先に結論
- 10月はキット導入と体験の聞き取りの月でした。公開記事は1本です（aurora-packing-list）。
- 体験メモは6つできました。関門1（2026-11-10、記事5本）までは、あと4本必要です。
- アクセス・検索の数字は取れていません（APIトークン・認証情報が未設定のため）。
- 11月は「体験のいらない auto 記事で本数を確保する」と「体験がそろった approve 記事を承認に回す」を並行します。

## 1. アクセス（GoatCounter）
- **数字なし（APIトークン未設定）**。環境変数 `GOATCOUNTER_TOKEN` がありません。
- 計測タグ自体は入っています（`index.html`・`rovaniemi.html`・`blog/index.html`・`blog/aurora-packing-list.html` に `gaaasuu2013.goatcounter.com/count`）。トークンを登録すれば、10月分からさかのぼって取れる見込みです。
- 公開URL https://gaaasuu2013-prog.github.io/aurora/blog/aurora-packing-list.html には、この環境から接続できました（HTTP 200、2026-11-01）。

## 2. 検索（Search Console）
- **数字なし（認証情報未設定）**。
- 次の3項目は、数字がないため今月は出せません。
  - 伸びた記事：数字なし
  - 表示は多いがクリックが少ない記事：数字なし（→ タイトル・説明文の手直しは今月は行いません）
  - 11〜20位の検索語：数字なし
- 補足：ルートに `google8e9b8713f6780e42.html` があり、github.io 側で所有権確認はしてあるようです。独自ドメイン（kyokko-navi.com）へ移ったら登録し直しが必要です（strategy の段階2）。

## 3. 記事
| 項目 | 数 | 中身 |
|---|---|---|
| 公開記事（`status: ready`） | 1本 | aurora-packing-list（柱B・approve・2026-10-28公開、PR #4 を2026-10-29 Merge） |
| 下書き（`status: draft`） | 0本 | — |
| 調査メモ | 2件 | aurora-packing-list（完成）、ry-rental-suitcase（**未完成**：公式サイトに接続できず、事実はすべて未確認） |
| SNS投稿案 | 1件 | aurora-packing-list（`status: draft`、写真がそろうまで投稿しない） |
| sitemap.xml の URL | 22件 | アプリ 20件（日英×観測地9＋トップ）、ブログ 2件（一覧＋記事1本） |

- 目標との差：2027-01 に15本 → いま1本（残り14本）。関門1（2026-11-10）の5本まで残り4本。
- WEEKLY_LIMIT は2本です。11-02週と11-09週で最大4本なので、関門1は**全部が予定どおり進んでぎりぎり**です。

## 4. 体験メモと写真
| 体験メモ | 主に使う記事 | 不足していること |
|---|---|---|
| 2026-10-airport-lounge.md | helsinki-airport-lounge | 羽田・ヘルシンキの写真、搭乗券も見せたか |
| 2026-10-aurora-photo.md | aurora-photo-smartphone | 自分で撮ってうまくいった1枚、手でピントを合わせたか |
| 2026-10-epos-card.md | priority-pass-card-guide | 年会費などは公式で確認（運営者に聞く必要はなし） |
| 2026-10-rovaniemi-aurora-tour.md | rovaniemi-aurora-guide ほか | Arctic GM の良かった点、カメラマン写真がどちらのツアーか、写真の利用条件 |
| 2026-10-rovaniemi-packing.md | aurora-packing-list（公開済み） | 全身の写真、外にいた時間、カイロの枚数 |
| 2026-10-suitcase-rental.md | ry-rental-suitcase | 写真（「あとで送る」） |

- 体験メモ：6件（README を除く）。strategy の段階1「体験メモ4つ以上」は達成。
- 写真：`content/notes/img/` に8枚。
  - 運営者の撮影 6枚：オーロラ2枚（1枚はピンぼけ、1枚は iPhone の失敗）、ウィーンのラウンジ4枚。
  - ツアーのカメラマン撮影 2枚（`tour-cameraman` 入り）。**どちらのツアーかが未回答**のため、まだ記事に使えません（ルール7の撮影者表記ができない）。

## 5. 運営者への質問（`data/questions.md`）
- 全51問：回答済み 42、**未回答 9**（月報作成前の数）。
- 今回、新しい候補2本の分として7問を追加しました（寝台列車4問、中欧の旅程3問）。追加後の未回答は16問です。
- いちばん効く質問3つ
  1. カメラマンの写真2枚は、それぞれどちらのツアー（Beyond Arctic／Arctic GM）？ ツアー会社の案内に写真の利用について何か書いてあった？ → これでロヴァニエミ・ツアー・撮影の3記事に写真が使えるようになります。
  2. カメラマンに教わったあと、自分で手でピントを合わせて撮った？ 自分で撮った中で一番うまく撮れた1枚はある？ → aurora-photo-smartphone の最後の不足。
  3. Arctic GM の良かった点は？（オーロラが出るまで続行する点をどう感じたか） → ツアー比較を公平に書くために必要。

## 6. 紹介リンク台帳（`data/affiliates.md`）
| 項目 | 数 |
|---|---|
| 登録された案件 | 8件 |
| 提携済み | 1件（エポスカード、A8.net、2026-10-29。バナーのみ、テキストリンクは作れない） |
| ASP・作り方が未確定（「要確認」「見つからず」） | 7件 |
| 公開可 | **0件**（独自ドメインへ移るまで「まだ」） |

- `tools/build_blog.py` の `SITE` はまだ github.io です。このままだと紹介リンクつきの記事はビルドが止まります（ルールどおり）。
- 10月に A8.net で探して見つからなかった案件：Rentio、プライオリティパス付きカード（2026-10-29）。

## 7. 見張り（`data/watchlist.md`）
- 見張り係はまだ一度も動いていません（週報 `weekly-*.md` が0件）。
- 7項目のうち、前回の値があるのは4項目で、どれも**まとめ記事（jafit.jp）からの転記**です。公式との照合が必要です（要確認）。
- アールワイレンタル・Rentio・紹介案件の3項目は値が空です。

## 8. 初期設定の進み具合（`data/strategy.md`）
| 状態 | 数 | 項目 |
|---|---|---|
| 済み | 5 | キット導入、体験メモ、スケジュールタスク3つ、副業ルール確認（申請は未確認）、ドメイン名決定 |
| 一部済み | 2 | ASP登録（A8.netのみ。バリューコマース・もしもは未）、独自ドメイン（取得済み 2026-10-31・移転は未） |
| 未確認 | 2 | GoatCounter APIトークン、Open-Meteo 有料プラン |

## 9. 作業の量（git log）
- 10月のコミット：69件（うち件名に「体験メモ」を含むもの 28件）。
- プルリクエスト：4件、すべて Merge 済み（#1 キット v2、#2 /go・/status、#3 strategist、#4 aurora-packing-list）。開いている PR は0件。
- ブランチ `claude/aurora-packing-list` が、Merge 後もローカル・リモートに残っています（消してよいかは運営者の判断）。

## 10. バックログの並び替え（`data/backlog.md` に反映済み）
考え方
- 11〜12月はオーロラの本番シーズン。strategy の方針どおり、A観測地・B準備を上に、C空港・カードを下げました。
- 関門1・2の本数を落とさないよう、体験のいらない auto 記事（Kp指数、観測地比較、時間帯）を上位に置きました。
- 体験がそろっている approve 記事（スーツケース、ロヴァニエミ）はその次。承認待ちが溜まりすぎないよう、週1本ずつのペースを想定しています。
- 新しい候補を6本足しました。体験が必要なものは「必要な体験」欄に書き、足りない分の質問を `data/questions.md` に足しました。

主な変更
- 上げた：kp-index-guide（3→1）、aurora-destinations-compare（6→2）、rovaniemi-aurora-guide（7→4）、aurora-best-time-night（12→5）
- 下げた：helsinki-airport-lounge（5→14）、priority-pass-card-guide（8→16）。C柱は4〜8月が本番で、紹介リンクもまだ使えないため。
- 区分を変えた：aurora-tour-or-diy を auto → approve 見込みに（ツアー2社の体験メモができたため）。
- 公開済みの aurora-packing-list は表の下の「公開済み」へ移しました。
- 追加（6本）：rovaniemi-aurora-tour-review、rovaniemi-december-guide、aurora-camera-rental、kyokko-navi-howto、helsinki-rovaniemi-night-train、aurora-central-europe-route

## 11. 来月（2026-11）の重点3つ
1. **関門1（記事5本）を11月中旬までに越える。** kp-index-guide → aurora-destinations-compare を auto で出し、ry-rental-suitcase と rovaniemi-aurora-guide を承認に回す。ry-rental-suitcase は公式サイトの再調査から（今回、この環境から github.io に接続できたので、許可ドメインを確かめてから再挑戦）。
2. **数字を取れるようにする。** GoatCounter の APIトークン登録（運営者の初期設定）。独自ドメインへ移ったら Search Console の登録し直しと、こちらへの認証情報の設定。来月の月報から「伸びた記事」「11〜20位の検索語」が出せるようになります。
3. **写真の質問を1回の /trip-log で片づける。** カメラマン写真のツアー名と利用条件、自分で撮った1枚、スーツケースの写真。これで4記事の写真の不足が解けます。
