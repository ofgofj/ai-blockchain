---
title: "Zcashで4件の脆弱性が発覚し修正、開発チームが協調対応"
source: "https://www.neweconomy.jp/posts/566516"
published: Mon, 20 Apr 2026 07:48:38 +0000
tags:
  - blockchain
---

ユーザー資金への影響なし
Zcash開発の独立組織であるZcashオープンディベロップメントラボ（Zcash Open Development Lab：ZODL）とZcash財団（Zcash Foundation）が、ZcashのフルノードソフトウェアであるzcashdおよびZebraに複数の脆弱性が発見・修正されたことを公式ブログで4月17日に発表した。
今回報告された脆弱性は計4件。いずれもセキュリティ研究者のアレックス・スカラー・ソル（Alex &#8220;Scalar&#8221; Sol）氏が2026年4月4日にシールデッドラボ（Shielded Labs）へ報告したもので、同氏は今年3月にも別のZcash脆弱性を報告した人物と同一人物だ。
1つ目は、Zcashの最先端プライバシープロトコルであるオーチャード（Orchard）ノードのクラッシュだ。特定のOrchardトランザクションを受信したzcashdおよびZebraのノードがパニックしてクラッシュする脆弱性。攻撃者が細工したトランザクションをブロードキャストすることで、ネットワーク上の任意のノードを停止させることができた。
2つ目は、コンセンサスの乖離によるチェーン分岐リスクだ。epk（エフェメラル公開鍵）の検証においてzcashdとZebraの実装に差異があり、特定のトランザクションに対して両実装が異なる判断を下す可能性があった。悪用されれば意図的なチェーン分岐を引き起こすことができた。
3つ目は、ターンスタイルの無効化だ。重複ブロックヘッダーの受信によって、プール残高の追跡・強制機能である「ターンスタイル」が無効化されるバグで、zcashd v5.10.0で混入したものだという。通常のP2Pネットワーク動作でも発生し得るほか、悪意あるピアによって意図的に引き起こすことも可能だった。ただし本脆弱性単独ではZECの偽造・窃取はできず、別途残高脆弱性が必要になる。
4つ目は、整数オーバーフローによる未定義動作だ。プール残高計算において符号付き整数のオーバーフローが発生し得る状態にあった。C++では符号付き整数オーバーフローは未定義動作であり、コンパイラの最適化によってターンスタイル検証がスキップされるリスクがあった。
シールデッドラボは報告受領後、ただちにZODLおよびZcash財団と連携。ZODLのクリス・ナッティコム（Kris Nuttycombe）氏とダイラ＝エマ・ホップウッド（Daira-Emma Hopwood）氏がパッチを開発し、Zcash財団のコンラード・ゴウヴェア（Conrado Gouvêa）氏がZebra向けのパッチを担当した。なお発表では、脆弱性分析および修正の一部にClaude Opus 4.6を活用したことも明記されている。
その後、ViaBTC・Luxor・F2Pool・AntPool（zcashd使用）およびFoundry（Zebra使用）などの主要マイニングプールへ事前にパッチが展開され、公開開示前にネットワークの圧倒的多数のハッシュパワーが保護された状態となった。
発表によれば、いずれの脆弱性もコンセンサスチェーンへの影響に利用された形跡はなく、ユーザー資金の安全性とプライバシーは損なわれていないとしている。ZECの供給量増加につながるような悪用も確認されていない。修正済みバージョンはzcashdがv6.12.1、Zebraがv4.3.1で、両実装のユーザーは速やかにアップデートすることが推奨されている。
今回の開示はZcashエコシステムにとって1ヶ月以内で2度目の脆弱性開示となった。ZODLは「深刻なセキュリティ調査を受け、それを適切に処理できる体制がZcashエコシステムに整いつつあることを示している」とコメントしている。

Security Disclosure: We&#8217;ve released zcashd v6.12.1, and the Zcash Foundation has released Zebra v4.3.1, addressing four vulnerabilities – including an Orchard action-encoding bug that could crash nodes and a related consensus-split issue between the two clients. Mining pools…
— Zcash Open Development Lab (@zodl_co) April 17, 2026

参考：発表　画像：PIXTA
関連ニュース

 Zcash向け機関投資家マイニングプール、大手ファウンドリーが4月開始へ
Zcash向けUI開発のZODL、25Mドル調達、サイファーパンクやa16zら出資
ヴィタリック、Shielded Labsに再び寄付。Zcashのコンセンサス強化「Crosslink」開発支援で
 ウィンクルボス兄弟、Zcash開発組織「シールデッド・ラボ」に3221ZECの寄付
プライバシー重視のケーキウォレットがZcashに対応、シールド取引がデフォルトに
