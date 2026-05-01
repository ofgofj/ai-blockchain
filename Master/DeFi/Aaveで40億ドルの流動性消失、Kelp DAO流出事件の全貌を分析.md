---
title: "Aaveで40億ドルの流動性消失、Kelp DAO流出事件の全貌を分析"
source: "https://crypto-times.jp/news-4-billion-in-liquidity-lost-at-aave/"
published: Tue, 28 Apr 2026 08:27:17 +0000
tags:
  - blockchain
---

オンチェーン分析プラットフォームのGlassnodeはKelp DAOのrsETHブリッジで発生したハッキング事件と、それに伴うDeFi大手Aaveへの深刻な影響に関する詳細なレポートを公開しました。

Aave V3 lost $4.0B in available liquidity in 29 hours after the Kelp DAO rsETH bridge exploit.

WETH utilization hit 100% in 1.4 hours, seven hours before the Protocol Guardian&#8217;s freeze. The contracts held throughout. The bridge did not.

Read the full report &#x1f447;… pic.twitter.com/pMxifJmfIP

— glassnode (@glassnode) April 27, 2026

事件の発端はLayerZeroのメッセージ偽造により、Kelp DAOから11万6,500 rsETHが不正に流出したことです。LayerZeroの事後報告によると検証者が依存していた2つのRPCノードが事前に侵害され、さらにバックアップのエンドポイントへのDDoS攻撃によって攻撃者が制御するノードへのフェイルオーバーが強制されたことが原因とされています。

これにより、ソース側でのバーン（焼却）を伴わない偽造パケットが検証を通過しました。

(adsbygoogle = window.adsbygoogle || []).push({});

関連記事：たった46分間でKelpDAOより410億円が流出、週末には1兆円が市場から流出したDeFi最大の事件は何が問題だったのか

流出したrsETHはAave V3、Compound V3、Eulerなどのレンディングプロトコルに担保として供給されました。特にAave V3では攻撃者が7つのアドレスを使用して8万9,567 rsETHを供給し、E-Mode下で最大93%のLTV（担保価値比率）を適用して約1億9,300万ドル相当のWETHおよびwstETHを借り入れました。

この動きによりAave V3の利用可能な流動性はわずか29時間で40億ドル減少。特にWETHの利用率はプロトコル・ガーディアンによる凍結措置が取られる7時間前の時点で、わずか1.4時間で100%に達しました。

(adsbygoogle = window.adsbygoogle || []).push({});

今回の事件で注目すべきはChainlinkのオラクル自体は正常に動作していた点です。オラクルはrsETHをETHの償還率に基づいて正しく価格設定していましたが、ブリッジ層で資産の裏付けが瞬時に失われたことを検知する仕組みがなかったため自動清算エンジンが作動しませんでした。

今回の事件は、ブリッジの脆弱性がDeFiエコシステム全体に波及するリスクを改めて浮き彫りにしました。4月だけで5億ドルを超える仮想通貨ハッキング被害が発生しており、分散型金融の安全性が改めて問われています。

Triaカードは世界中で使える仮想通貨クレジットカード (約3000円〜) で、最大6%が仮想通貨でキャッシュバックされます。

仮想通貨での資産運用もカード管理アプリから行えます。早期利用者にはさらなる報酬も用意されているため是非この機会に登録しておきましょう。（登録に必要なアクセスコード：MWVJXJ6475）

©Crypto Times. All rights reserved.
