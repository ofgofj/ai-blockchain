---
title: "スイのDeFiプロトコル「アフターマス」で資金流出、手数料ロジックの脆弱性突かれ約113万ドル被害"
source: "https://www.neweconomy.jp/posts/570532"
published: Fri, 01 May 2026 09:40:15 +0000
tags:
  - blockchain
---

Aftermathのデリバティブ機能でエクスプロイト
レイヤー1ブロックチェーン「スイ（Sui）」上の分散型金融（DeFi）プロトコル「アフターマス（Aftermath Finance）」で、プロトコルに影響を及ぼすエクスプロイトが明らかになった。同プロトコルの公式Xが4月29日に発表した。
Xの発表によると同プロトコルはユーザー資金への影響を最小限に抑えるため、予防措置として一時停止された。同プロトコルの開発チームは、セキュリティパートナーと連携し調査が進めるという。
その後の発表で同チームは、スイの主要開発企業ミステンラボ（Mysten Labs）およびスイ財団（Sui Foundation）の支援により、すべてのユーザーが全額補償される見込みであると明らかにした。
その後、アフターマス開発チームは5月1日、事後分析（ポストモーテム）を公表した。分析によると、今回の事象は同プロトコルのデリバティブ取引機能「AFパープス（AF Perps）」のインテグレーター機能において発生したものだという。
通常、取引を行うユーザーは手数料を支払うが、今回のケースではその手数料が「マイナスの値」として設定できる状態になっていた。その結果、本来は支払うはずの手数料が逆にユーザーに付与される形となり、取引を行うほど資金を受け取れる状態が生じていたと同チームは説明している。
なお、Move言語ではトークンなどの資産は「リソース」として扱われており、リソース型においては負の値を持つことや不正に増減させることができない設計となっている。これにより、資産そのものが不正に生成されるような挙動は防がれる仕組みだ。
一方で今回問題となったのは資産そのものではなく、手数料の計算ロジックだった。手数料は通常の数値として扱われており、負の値を設定できる状態となっていた。
同チームの分析によると、攻撃者はこの仕組みを利用し、自身をインテグレーターとして登録したうえで負の手数料を設定したという。その上で利益が発生する取引を繰り返し実行し、資金を引き出したとみられている。
また同チームは、攻撃は複数回にわたり実行され、合計で約113万9,000ドル（約1.79億円）相当のUSDCが流出したと説明している。
同チームによると、この問題は2025年8月のコード変更で導入され、同年11月の監査でも検出されていなかったという。
攻撃者はその後、資金を複数のウォレットや分散型取引所（DEX）を通じて移動し、中央集権型取引所へ送金したとされる。
同チームはアフターマスの今後について、AFパープスの再開に向けて追加監査を実施する方針だ。また、2026年においては手動レビューのみでは不十分であるとの認識を示し、AIを活用したセキュリティ体制の強化に取り組む方針を示している。

Attention Aftermath community &#8211; We’ve identified an exploit affecting the protocol.Our team is actively investigating alongside leading security partners. As a precaution, the protocol has been paused and measures are being taken to minimize potential impact to user funds.…
— Aftermath Finance (, ) (@AftermathFi) April 29, 2026


Update: Great news. Thanks to support from @Mysten_Labs and @SuiFoundation all users will be made whole ZERO losses for anyone.Aftermath will be up and running again soon. Thank you to both teams and to @blockaid_ for the rapid response.For clarity: this was not a Move…
— Aftermath Finance (, ) (@AftermathFi) April 29, 2026


Aftermath PostmortemOn April 29th, Aftermath experienced an isolated security incident in the integrator feature of AF Perps.All other products (afSui, Pools, Farms, Agg, SOR) are completely unaffected &amp; all users will be made whole.This has been a scary week for crypto. AI…
— Aftermath Finance (, ) (@AftermathFi) April 30, 2026

画像：PIXTA
関連ニュース

 【取材追記】スイのレンディング「Scallop」でインシデント発生、約15万SUIが不正流出
 SuiのDEX「Cetus」、約321億円相当のハッキング被害。約234億円超を凍結と報告
スイ上のVolo Protocolでエクスプロイト、約350万ドル規模の被害。一部資産は凍結成功
スイの「Typus Finance」で約5.3億円相当のハッキング被害
スイ上のDeFi「ネモプロトコル」、240万ドルのエクスプロイト攻撃被害
