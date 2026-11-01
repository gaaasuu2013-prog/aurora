# 調査メモ：Kp指数とは？オーロラ予報の読み方（確認日 2026-11-01）

- slug：kp-index-guide / pillar D / tier auto（体験なし・お金の話なし）
- 「公式か」の欄：公式＝運営主体（NOAA SWPC、GFZ、NICT など）の公式ページ／公的＝政府・大学・公的研究機関の発表や資料／非公式＝まとめ・民間サイト（要公式確認）
- 注意1：NOAA SWPC のWebサイトは `www.swpc.noaa.gov` から `www.spaceweather.gov` に移っています（2026-11-01 に 301 転送を確認）。記事の「参考」には spaceweather.gov のURLを使うこと。データ配信の `services.swpc.noaa.gov` はそのまま。
- 注意2：この調査で、極光ナビが使っている太陽風データのURLが 404 になっていることを見つけました（下の「極光ナビでの見方」の最後を参照）。記事に「極光ナビで Bz を見られる」と書く前に、アプリ側の確認が必要です。

## 狙う検索語
実際に検索した語に ✔。
- ✔ Kp指数とは オーロラ
- ✔ オーロラ予報 見方 Kp
- ✔ Kp指数 いくつで見える 日本 北海道 オーロラ
- ✔ オーロラ予報 サイト NOAA 見方 解説
- ✔ Kp指数 見方 3日予報 オーロラ 旅行
- ✔ オーロラ 見える条件 Kp 雲 月明かり 予報 アプリ
- ✔ オーロラ 予報 見方 Kp指数 OVATION 30分予報 ブログ
- ✔ Kp指数 オーロラ フィンランド アイスランド 目安 いくつ
- ✔ NICT 宇宙天気 オーロラ 日本 見える 低緯度オーロラ 解説
- ✔ 国立極地研究所 2024年5月 オーロラ 北海道 磁気嵐 観測

本命：「Kp指数とは」「オーロラ 予報 見方」「Kp指数 いくつ 見える」。サブ：「Kp 北海道」「OVATION 見方」「Bz オーロラ」「オーロラ 27日予報」。

## 上位記事が答えていること / 答えていないこと
日本語の上位は「天文観測完全ガイド」（xn--29sob207cg49a.com）の記事が多数を占めていました。ただし本文は 403 で開けず、検索結果の抜粋しか見ていません（＝数字は採っていない）。

本文を開いて読んだ記事：
1. Guide to Iceland（日本語）「アイスランドでオーロラを見る方法」 https://guidetoiceland.is/ja/the-northern-lights/how-to-find-the-northern-lights-in-iceland （非公式）
2. NOAA SWPC「Tips on Viewing the Aurora」 https://www.spaceweather.gov/content/tips-viewing-aurora （公式）
3. NOAA NCEI「How Science Predicts the Aurora」 https://ncei.noaa.gov/news/chasing-northern-lights （公式、2017-12-07 公開、2024-12-20 更新）
4. NICT オーロラ・アラート https://aurora-alert.nict.go.jp/ （公式）
（開けなかった：天文観測完全ガイドの各記事＝403）

答えていること
- Kp は 0〜9 で地磁気の乱れを表す。数字が大きいほど南（低緯度）まで見える（全記事）。
- Kp ごとの「見え方」の目安の表（Guide to Iceland：Kp2 で淡い、Kp5〜6 で磁気嵐など）。※出典のない独自の目安。
- 日本（北海道）は Kp 7 前後が目安、とする記事が多い（天文観測完全ガイドの抜粋）。※公的な出典は見つからず。
- Bz がマイナス（南向き）だと出やすい、太陽風が速いと明るい（Guide to Iceland）。
- 雲がないこと、月明かり、街明かりも必要（NCEI、Guide to Iceland）。
- 予報は3日先まで、それ以上は当てにならない（Guide to Iceland）。

答えていないこと（＝私たちが書ける差）
- **Kp と「地磁気緯度」の関係。** 同じ Kp でも、地図の緯度ではなく地磁気緯度で見え方が決まる。NOAA は明記しているが、日本語記事はほぼ触れていない。
- **3日予報の数字の読み方。** 時刻が UT（世界時）であること、「4.67」のような小数は 1/3 刻みの値（5- のこと）であること、12時間ごと（00:30 と 12:30 UTC）に出ること。
- **予報の種類ごとの役割の違い。** 27日予報＝旅行日の目安、3日予報＝前日〜当日の判断、OVATION＝30〜90分先の「今、外に出るか」。それぞれの限界を公式の説明つきで並べた記事は見当たらない。
- **Kp が低くても見える場所がある。** 北ノルウェーやラップランドでは Kp が低くても出る（NOSWE/UiT）。フィンランド気象研究所の「晴れて暗い夜の何割で見えるか」の統計。
- **2026年5月に NOAA の「ビューライン」（見える南限の線）が廃止された**こと。古い記事はこの線の見方を書いている。
- **日本の「K指数」と「Kp指数」の違い。** NICT の宇宙天気予報の地磁気レベルは柿岡（茨城県）の K 指数で、Kp ではない。
- **北海道では「規模の大きくない磁気嵐」でも見えた例がある**（北海道大学・OIST の2026年5月の発表）。Kp だけでは決まらないことの公的な裏付け。
- **アプリが何を掛け合わせて判定しているか**（極光ナビのスコアの中身）。

## 使える事実
| 事実 | 値 | 出典URL | 確認日 | 公式か |
|---|---|---|---|---|
| Kp の定義（SWPC） | 「13の地磁気観測所の標準化した K 指数の平均」。3時間の磁力計の水平成分の最大変動から求める。0〜9、1 が静穏、5 以上が磁気嵐 | https://www.spaceweather.gov/products/planetary-k-index | 2026-11-01 | 公式 |
| SWPC の Kp は「推定値」 | SWPC のリアルタイム値は「Estimated 3-hour Planetary Kp-index」。8か所の磁力計（Sitka, Meanook, Ottawa, Fredericksburg, Hartland, Wingst, Niemegk, Canberra）から推定。公式な Kp は GFZ のページを案内 | https://www.spaceweather.gov/products/planetary-k-index | 2026-11-01 | 公式 |
| Kp の尺度は 1/3 刻み、K は準対数 | NCEI：「The scale is 0 to 9 expressed in thirds of a unit」、K 指数は「quasi-logarithmic」（準対数）の局所指数。Kp は13観測所の平均 | https://www.ncei.noaa.gov/products/geomagnetic-indices | 2026-11-01 | 公式 |
| Kp の考案と算出機関 | 1949年に Julius Bartels が導入。13の地磁気観測所のデータにもとづく。データ出典は GFZ（ドイツ地球科学研究センター） | https://kp.gfz.de/en/ | 2026-11-01 | 公式 |
| GFZ の Kp は国際的に公認 | 「国際地球電磁気学・超高層物理学協会（IAGA）が承認した公式の Kp」。準リアルタイムの nowcast 値と、月ごとの確定値（definitive）を出す | https://kp.gfz.de/en/about-kp | 2026-11-01 | 公式 |
| Kp と G スケール | G1（Minor）＝Kp5、G2（Moderate）＝Kp6、G3（Strong）＝Kp7、G4（Severe）＝Kp8（9- を含む）、G5（Extreme）＝Kp9 | https://www.spaceweather.gov/noaa-scales-explanation | 2026-11-01 | 公式 |
| G スケールの頻度（11年周期あたり） | G1：1700回（900日）、G2：600回（360日）、G3：200回（130日）、G4：100回（60日）、G5：4回（4日） | https://www.spaceweather.gov/noaa-scales-explanation | 2026-11-01 | 公式 |
| G スケールとオーロラが見えた範囲 | G1：高緯度でふつうに見える（米ミシガン北部・メイン）／G2：ニューヨーク・アイダホまで（地磁気緯度 約55°）／G3：イリノイ・オレゴンまで（約50°）／G4：アラバマ・北カリフォルニアまで（約45°）／G5：フロリダ・テキサス南部まで（約40°） | https://www.spaceweather.gov/noaa-scales-explanation | 2026-11-01 | 公式 |
| Kp とオーバルの南端 | Kp0 でオーロラ帯（オーバル）の赤道側の端は約66°、Kp が1上がるごとに約2°南へ、Kp9 で約48°（いずれも地磁気緯度）。「地理の緯度ではなく地磁気緯度で成り立つ」 | https://www.spaceweather.gov/content/tips-viewing-aurora | 2026-11-01 | 公式 |
| Kp と緯度の関係は平均 | 「おおよそで平均を表す」「厳密に成り立たないときもある」。Kp ごとの図は「オーロラがある場所ではなく、見ることができる地点」を示す | https://www.spaceweather.gov/content/tips-viewing-aurora | 2026-11-01 | 公式 |
| よく見える時間帯 | 真夜中の前後1〜2時間（現地時間 22時〜2時） | https://www.spaceweather.gov/content/tips-viewing-aurora | 2026-11-01 | 公式 |
| 季節 | 春分・秋分のころがよい。ただし春分・秋分の前後は暗い時間の長さが急に変わる | https://www.spaceweather.gov/content/tips-viewing-aurora | 2026-11-01 | 公式 |
| 月 | 満月はオーロラの「見かけの」明るさを下げる（実際の明るさではない） | https://www.spaceweather.gov/content/tips-viewing-aurora | 2026-11-01 | 公式 |
| 雲・暗さ | 「空が晴れて雲がないこと」「暗いこと」が必要。オーロラ帯の夏は白夜で見られない。よく見える帯は南北の緯度 約60〜75° | https://www.spaceweather.gov/phenomena/aurora | 2026-11-01 | 公式 |
| 雲・月・街明かり（NCEI） | 雲は天気予報で確認。満月は背景の空が明るくなり見えにくい。街明かり・天気・月などが見え方に影響。宇宙天気も天気も何週間も先は予報が難しい | https://ncei.noaa.gov/news/chasing-northern-lights | 2026-11-01 | 公式 |
| 3日予報の発表 | 1枚の文章の予報。12時間ごと、00:30 と 12:30 UTC に発表 | https://www.spaceweather.gov/products/3-day-forecast | 2026-11-01 | 公式 |
| 3日予報の中身（実物） | 「NOAA Kp index breakdown」で3日×8枠（00-03UT〜21-00UT）の Kp。例：2026-11-01 12:30 UTC 発表分で「The greatest expected 3 hr Kp for Nov 01-Nov 03 2026 is 4.67 (NOAA Scale G1)」 | https://services.swpc.noaa.gov/text/3-day-forecast.txt | 2026-11-01 | 公式 |
| 27日予報の発表と中身 | 10.7cm 太陽電波、Ap 指数、「その日の最大 Kp」の数値予報。毎週月曜 15:00 UTC までに発表 | https://www.spaceweather.gov/products/27-day-outlook-107-cm-radio-flux-and-geomagnetic-indices | 2026-11-01 | 公式 |
| 27日予報の実物 | 例：「:Issued: 2026 Oct 26 0118 UTC」、列は日付・Radio Flux・Planetary A Index・Largest Kp Index | https://services.swpc.noaa.gov/text/27-day-outlook.txt | 2026-11-01 | 公式 |
| 27日周期の考え方 | SWPC：太陽の27日の自転周期にわたる活動領域の「持続と再来」が予報に重要。※27日予報の精度の公式説明は**未確認** | https://www.spaceweather.gov/forecasts | 2026-11-01 | 公式 |
| OVATION とは | ジョンズ・ホプキンス大学 応用物理研究所が開発した、オーロラの強さの経験モデル（OVATION Prime）。SWPC が2020年に運用開始 | https://www.spaceweather.gov/products/aurora-30-minute-forecast | 2026-11-01 | 公式 |
| OVATION の先読み時間 | 「30〜90分先」のオーロラの位置と強さ。先読みの長さは太陽風が L1（地球の約160万km手前）から地球に届くまでの時間で決まる | https://www.spaceweather.gov/products/aurora-30-minute-forecast | 2026-11-01 | 公式 |
| OVATION の限界 | 太陽風データが欠けたり乱れたりすると、現在の Kp で代用し「先読み時間はなくなる」。元のモデルは Kp7 までしか信頼できず、2013年の改良で Kp8・9 まで拡張 | https://www.spaceweather.gov/products/aurora-30-minute-forecast | 2026-11-01 | 公式 |
| OVATION の確率の意味 | 「見える確率」はオーロラの強さと直線的な関係にあると仮定して出した推定 | https://www.spaceweather.gov/products/aurora-30-minute-forecast | 2026-11-01 | 公式 |
| 遠くからでも見える | 明るく条件がよければ最大 約1000km 離れた場所から見える | https://www.spaceweather.gov/products/aurora-30-minute-forecast | 2026-11-01 | 公式 |
| OVATION の実データ例 | 2026-11-01 取得分：Observation Time 13:09Z、Forecast Time 14:05Z（この回は約56分先）。形式は［経度, 緯度, オーロラ値］ | https://services.swpc.noaa.gov/json/ovation_aurora_latest.json | 2026-11-01 | 公式 |
| 今夜・明晩の予報図 | 「Aurora for Tonight and Tomorrow Night (Experimental)」。OVATION に、米国中部時間 18時〜6時の3日予報の最大 Kp を入れて作る | https://www.spaceweather.gov/products/aurora-viewline-tonight-and-tomorrow-night-experimental | 2026-11-01 | 公式 |
| ビューライン廃止 | 「In May 2026, the viewline was removed」（2022年に追加された見える南限の線を、2026年5月に削除） | https://www.spaceweather.gov/products/aurora-viewline-tonight-and-tomorrow-night-experimental | 2026-11-01 | 公式 |
| Bz（南向き磁場）の役割 | 磁気嵐には、南向きの磁場が最も重要。太陽風のエネルギーを磁気圏へ運ぶのに効果的。高速の太陽風が数時間以上続くことも条件 | https://www.spaceweather.gov/phenomena/geomagnetic-storms | 2026-11-01 | 公式 |
| CME の到着時間 | 速いものは 15〜18時間、遅いものは数日。速さは 250km/s 未満〜3000km/s 近く。南向きの磁場が強く長く続くほど強い嵐。L1 の衛星で衝撃波の到着を 15〜60分前に知らせられる | https://www.spaceweather.gov/phenomena/coronal-mass-ejections | 2026-11-01 | 公式 |
| 太陽風の速さ | ふつう（低速風）は 約400km/s。コロナホールからの高速風は 500〜800km/s | https://www.spaceweather.gov/phenomena/solar-wind | 2026-11-01 | 公式 |
| 太陽風を測る衛星 | ACE（1998-02-16〜）、DSCOVR（2016-07-27〜）、SOLAR-1（2026〜）、IMAP I-ALiRT（2026〜）。SOLAR-1 と IMAP が ACE・DSCOVR に置き換わる | https://www.spaceweather.gov/products/real-time-solar-wind | 2026-11-01 | 公式 |
| Bz の表示（SWPC） | リアルタイム太陽風のグラフは Bz < 0 nT を色付け（設定で Bz < -5 nT に変更可）。※「何 nT ならよい」という公式の基準は**未確認** | https://www.spaceweather.gov/products/real-time-solar-wind | 2026-11-01 | 公式 |
| NICT：IMF の向き | IMF（惑星間空間磁場）が南向きになるとオーロラが明るくなる。オーロラ・アラートは DSCOVR の太陽風データと AE 指数から世界全体の活動度を4段階で表示 | https://aurora-alert.nict.go.jp/ | 2026-11-01 | 公式 |
| NICT：予報カレンダー | オーロラ活動の約27日周期にもとづく経験モデル。予測マップは地磁気緯度 約60°より低緯度側は出ない（日本上空は示さない） | https://aurora-alert.nict.go.jp/ | 2026-11-01 | 公式 |
| NICT の地磁気レベルは K 指数（柿岡） | NICT 宇宙天気予報の地磁気擾乱レベルは、気象庁地磁気観測所（茨城県石岡市柿岡）の K 指数で5段階：K4未満＝静穏、4＝やや活発、5＝活発、6＝非常に活発、7以上＝猛烈に活発。Kp ではない | https://swc.nict.go.jp/knowledge/criteria_icon.html ・ https://swc.nict.go.jp/trend/geomag.html | 2026-11-01 | 公式 |
| 2024年5月の G5 | SWPC：G5 は 2024-05-10 午後6:54（米東部夏時間）に初めて観測（発表 23:58 UTC）。G5＝Kp9（G スケールの定義より） | https://www.spaceweather.gov/news/g5-conditions-observed | 2026-11-01 | 公式 |
| 2024年5月の位置づけ | NOAA：「今世紀に記録された中でおそらく最強の磁気嵐」、G5 は「スケールの最上位」 | https://www.noaa.gov/heritage/stories/five-historically-huge-solar-events | 2026-11-01 | 公式 |
| 2024年5月11日 日本のオーロラ | 国立極地研究所ほか（2024-10-31 発表）：日本の広い範囲から市民が撮った179点の写真を分析。兵庫県など低緯度でも見えたのは、発光が高度 約1,000km まで達したため。色は赤でなくマゼンタ。写真は北海道・東北・中部などから。論文：Scientific Reports, doi:10.1038/s41598-024-75184-9 | https://www.ism.ac.jp/ura/press/ISM2024-02/pr20241031.pdf | 2026-11-01 | 公的 |
| 2024年5月11日の報道 | ウェザーニュース（2024-05-12）：5月11日夜、北日本や北陸などから観測報告。北海道では肉眼でもうっすら見えた所があった。北の低い空が赤〜ピンク | https://weathernews.jp/news/202405/120045/ | 2026-11-01 | 非公式（報道） |
| 規模が大きくない嵐でも北海道で見えた | 北海道大学・OIST（2026-05-21 発表）：2024-06-28、08-04、09-12、11-09、2025-03-26 の5回、規模があまり大きくない磁気嵐で北日本に低緯度オーロラ。いずれも太陽風の密度が非常に濃く（30〜70個/cc、通常の約10倍）、磁気圏が強く圧縮されたとき。発光高度 500〜800km（通常の赤いオーロラは約200km）。論文：J. Space Weather Space Clim., doi:10.1051/swsc/2026004 | https://www.hokudai.ac.jp/news/pdf/260521_pr.pdf | 2026-11-01 | 公的 |
| 陸別の地磁気緯度 | 北海道陸別の地磁気緯度 約36.9°。2025-03-26 22:27〜23:12（日本時間）にオーロラ（名古屋大学 ISEE の研究集会資料） | https://cicr.isee.nagoya-u.ac.jp/hokkaido/workshop/r07/04_yoda.pdf | 2026-11-01 | 公的（研究者の発表資料） |
| 北海道で見える Kp の目安 | **未確認**。「Kp7 前後」とする民間記事はあるが、公的な出典は見つからず。書くなら「一律の数字はない」とし、上の北大発表を根拠にする | — | 2026-11-01 | — |
| 高緯度では Kp が低くても出る | NOSWE（ノルウェー宇宙天気センター、トロムソ大学）：北ノルウェーの地磁気は全球の状態と大きくずれることがあり、Kp が中程度でも地域の擾乱が起きる。サブストームは3時間の Kp よりずっと短い時間で起きる。ノルウェーでは全球でなく地域の値を見るのが大事 | https://site.uit.no/spaceweather/?p=3770 | 2026-11-01 | 公的 |
| フィンランドで見える割合 | フィンランド気象研究所：暗く雲のない夜のうち、キルピスヤルヴィ 75%、ラップランドのスキーリゾート（ユッラス、レヴィ、サーリセルカ）約50%、オウル・クーサモ 約25%、ヘルシンキ・トゥルク 月1回ほど。真夜中とその前後2時間ほどが多い。数値の Kp 基準はなく「場所ごとのしきい値」を超えると出やすい | https://en.ilmatieteenlaitos.fi/auroras-in-finland | 2026-11-01 | 公式 |
| Guide to Iceland の Kp 別目安 | Kp2 で淡いオーロラの可能性、Kp5〜6 で磁気嵐、など。Kp2 を超えれば外に出る価値あり。予報は最長3日 | https://guidetoiceland.is/ja/the-northern-lights/how-to-find-the-northern-lights-in-iceland | 2026-11-01 | 非公式（要公式確認。引用は避ける） |

## 読者の疑問リスト（見出し候補）
1. Kp指数とは？（0〜9、3時間ごと、地磁気の乱れ）
2. Kp はどこが出している？ NOAA の値と GFZ の値の違い（推定値と確定値）
3. 「4.67」って何？ 1/3 刻みの読み方（5- など）
4. Kp と G1〜G5 の対応表（磁気嵐の大きさ）
5. Kp いくつで見える？ → 「地図の緯度」ではなく「地磁気緯度」で決まる
6. フィンランド・ノルウェーなら Kp が低くても見える理由
7. 日本（北海道）で見るには？ 2024年5月の大磁気嵐と、規模が小さくても見えた例
8. 予報は3種類：27日予報（旅行日えらび）／3日予報（前日〜当日）／OVATION（30〜90分先）
9. 3日予報の読み方（UT の時刻を日本時間・現地時間に直す、12時間ごとの更新）
10. Bz と太陽風の速さ：いま出るかを見る指標
11. Kp が高くても見えない日：雲・月・暗さ・時間帯
12. NOAA の「ビューライン」が消えた（2026年5月）
13. 極光ナビでの見方（Kp・OVATION・雲の組み合わせ）

## 極光ナビでの見方（アプリのコードから読んだ要点。アプリは変更していない）
読んだファイル：/home/user/aurora/app.js、/home/user/aurora/index.html（「スコアの考え方」）

- **使っているデータ**
  - Kp：NOAA の `noaa-planetary-k-index-forecast.json`（観測値・推定値・予報値を3時間枠で取得）。グラフ「Kp指数 3日予報」に表示。観測・推定値は薄い色。Kp5〜6 を黄（G1〜G2）、Kp7 以上を赤（G3 以上）で色分け。
  - 27日予報：NOAA `27-day-outlook.txt` の「Largest Kp」を旅行日カレンダーに「Kp：NOAA 27日予報の最大値（目安）」として表示。画面の説明文は「オーロラの強さは3日より先は予報できません。暗い時間が長く月明かりの少ない夜を選び、出発直前にKp予報を確認しましょう」。
  - OVATION：NOAA `ovation_aurora_latest.json`（出現確率の地図）。
  - 太陽風：NOAA の Bz・速度（直近の平均）。
  - 雲：Open-Meteo の低層・中層・上層雲（1時間ごと、4日分）。
- **見えやすさスコア（0〜100）＝ 磁気活動 × 暗さ × 晴れ × 月明かり**（index.html の説明「確率ではありません」）
  - 磁気活動：観測地の地磁気緯度（双極子近似）から「地平線に見える目安の Kp」と「真上に来る目安の Kp」を計算し、Kp 予報と比べる。目安の式は、オーバルの赤道側の端が「Kp6 までは 66.5° − 2.05×Kp、それより上は 54.2° − 4.5×(Kp−6)」まで下がるとするもの。地平線の目安は真上より地磁気緯度で5°分ゆるい。
    - 参考：この式だと境界は Kp6＝54.2°、Kp7＝49.7°、Kp8＝45.2°、Kp9＝40.7°。NOAA G スケールの「見えた範囲」（G2 約55°、G3 約50°、G4 約45°、G5 約40°）とほぼ同じ。Kp0 の 66.5° は SWPC の「約66°」と近い。ただし Kp7 以上の下がり方は SWPC の「1あたり約2°、Kp9 で48°」より大きい（＝アプリは「見える地点」側の G スケールに合わせた形）。この対応はコードからの読み取りで、作者の意図は**未確認**。
    - 直近2時間だけ、Bz が −3nT より南向きなら Kp を上乗せ（最大 +1.5、太陽風が速いほど大きい）。
  - 暗さ：太陽高度 −5° から加点、−16° 以下で満点。
  - 晴れ：実効雲量＝低い雲ほど強く効く重み（低 1.0、中 0.85、上 0.45）。
  - 月明かり：月が出て明るいほど最大3割減点。
  - 判定の言葉：60以上「とても良い」系、35以上、15以上、それ未満の4段階（ラベル文言は I18N の vGreat / vGood / vMaybe / vLow）。
- **地図の「いま見えていそう」（別の判定）**：OVATION の出現確率（真上、または極側8°以内の最大値の6割）が10%以上、太陽が十分沈み、雲が多すぎない地点。OVATION が取れないときは Kp から推定したオーロラ帯で代用。
- **「いま外を見て」通知**：OVATION の値・暗さ・雲（60%未満／80%未満）と Bz（−10nT 以下、−6nT 以下）を組み合わせて2段階。通知オンのときは2分ごとに太陽風と OVATION を取り直す。
- **「いま」の欄**：Kp（5以上で「磁気嵐」表示）、Bz（南向き＝出やすい、−5nT 以下で強調）、太陽風速度（500km/s 以上で「速い」）、OVATION（真上／極側）、雲、太陽高度、月、地磁気緯度と「地平線の目安 Kp／真上の目安 Kp」。
- **陸別の例（手計算。アプリ画面で要確認）**：アプリの式で陸別（43.47°N, 143.75°E として計算）の地磁気緯度は約36°、地平線の目安 Kp は約9.0 になる。ISEE 資料の陸別の地磁気緯度 約36.9° と近い。北大の発表どおり、実際は Kp が低い日にも北海道で見えた例があり、アプリの目安は「大きな磁気嵐の目安」と書くのが安全。
- **見つけた問題（アプリ係への申し送り。記事に影響）**：アプリが太陽風に使う `https://services.swpc.noaa.gov/products/solar-wind/mag-2-hour.json` と `plasma-2-hour.json` が、2026-11-01 時点で **404**。`/products/` の一覧からも `solar-wind/` が消えている。代わりにあるのは `/products/summary/solar-wind-mag-field.json`（bt, bz_gsm, time_tag）、`/products/summary/solar-wind-speed.json`、`/json/rtsw/rtsw_mag_1m.json`、`/json/rtsw/rtsw_wind_1m.json`。このままでは、アプリの Bz 上乗せと Bz を使った通知は効かず、画面の Bz・太陽風速度は「取得できませんでした」になるはず（画面での確認は**未確認**）。Kp 予報・OVATION・27日予報のURLは 2026-11-01 に取得できた。
- 補足：Kp 予報の JSON は、いまは配列の配列ではなく `{time_tag, kp, observed, noaa_scale}` の形。observed の値は observed / estimated / predicted。アプリの読み込み（rows()）は両方の形に対応している。

## 体験メモで補ってほしいこと
- この記事は体験なし（tier auto）なので、必須の質問はありません。
- あれば使える任意の質問（auto を保つため、入れるなら別記事に回す）：ロヴァニエミでオーロラが出た夜、出発前に Kp 予報や極光ナビを見ていましたか？ そのとき Kp はいくつでしたか？（content/notes/2026-10-rovaniemi-aurora-tour.md にあれば、kyokko-navi-howto や観測地記事で使う）

## 書くときの注意
- 「北海道は Kp○以上で見える」と数字で言い切らない（公的な出典なし）。
- 「OVATION は30分予報」と書くなら「SWPC の説明では30〜90分先」と添える。
- ビューライン（見える南限の線）は2026年5月に廃止。古い説明を書かない。
- 3日予報・27日予報の時刻は UTC。日本時間・フィンランド時間への換算を書くなら、時差の出典を別に取る（このメモでは未取得）。
- 内部リンク候補：kyokko-navi-howto、aurora-best-time-night、aurora-moon-calendar、rikubetsu-aurora、aurora-destinations-compare（いずれもバックログ。公開済みかは要確認）。
