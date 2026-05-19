---
title: "THORChainが取引一時停止、約1070万ドル被害か。署名システム脆弱性の可能性浮上"
source: "https://www.neweconomy.jp/posts/574151"
published: Mon, 18 May 2026 06:43:51 +0000
tags:
  - blockchain
---

ソーチェーンでボールト侵害
クロスチェーン流動性プロトコル「ソーチェーン（THORChain）」が侵害を受けたとして、同チェーンの取引が一時停止した。オンチェーン調査者ザックXBT（ZachXBT）が自身のテレグラムグループで5月15日に報告した。その後、ソーチェーン公式Xアカウントでもインシデント発生を認める投稿が行われた。
ザックXBTによると、被害はビットコイン（Bitcoin）、イーサリアム（Ethereum）、BNBスマートチェーン（BNB Smart Chain）、ベース（Base）にまたがる可能性があるという。ブロックチェーンセキュリティ企業ペックシールド（PeckShield）も、約1,000万ドル（約15.9億円）相当の暗号資産（仮想通貨）が流出した可能性を指摘している。
ソーチェーンの発表によると、同プロトコルがクロスチェーン資産管理のために運用する6つの「アスガルド・ボールト（Asgard vault）」のうち1つが侵害された可能性があるという。被害額は現時点で約1,070万ドル（約17億円）規模と見積もられている。
また同報告によると、今回影響を受けたのはプロトコル保有資金であり、初期調査では個別ユーザーのスワップ資金被害は確認されていないとのこと。ネットワークは異常挙動を自動検知し、署名活動を停止したことで追加のアウトバウンド取引を防止したという。
その後もインシデントに関する追加報告がソーチェーン公式Xアカウントで公開された。
同報告によると、数日前にネットワークへ参加した新規ノードが攻撃に関与している可能性があるという。同プロトコルチームは、同ノード取得およびRUNEボンド用イーサリアム（Ethereum）アドレスと、盗難資金受領アドレスとの関連を確認したとしている。
また現時点での有力仮説として、複数ノードで秘密鍵管理を分散する署名システム「GG20 TSS（Threshold Signature Scheme）」実装に脆弱性が存在した可能性が挙げられている。この脆弱性により、ボールト参加者の秘密鍵情報が時間をかけて漏洩した可能性があるという。
さらにソーチェーンのプロトコルチームは、攻撃者が漏洩情報を蓄積することで、最終的にボールト管理用秘密鍵を再構築し、不正なアウトバウンド取引を実行した可能性があると説明している。
同プロトコルチームは、現在は法執行機関などと連携し、攻撃者特定と資金回収を進めているとのこと。
また同プロトコルチームは、「返金」、「エアドロップ」、「補償」などに関する偽アカウントや誤情報が拡散しているとして注意喚起も行った。現在、返金・補償プログラムは実施していないとしている。
なお、ソーチェーンを巡っては、過去にも複数の運営・セキュリティ問題が発生している。暗号資産メディア「ザ・ブロック（The Block）」によると、2025年1月には、債務超過懸念を背景としてレンディング機能「ソーファイ（ThorFi）」を停止し、90日間の再編対応を実施した。その後、約2億ドル（約318億円）規模の債務問題について、債務を新たなエクイティ型トークンへ転換する形で対応を進めていた。
また昨年9月には、ソーチェーン創設者ジョン・ポール・ソービョルンセン（John-Paul Thorbjornsen）氏の個人ウォレットから約120万ドル（約1.91億円）が流出した。

Important AnnouncementTrading on THORChain is currently halted after a vault was compromised. Initial indications are user funds are safe and only protocol owned funds are affected.The network automatically detected abnormal behavior and halted signing activity, which alerted…
— THORChain (@THORChain) May 15, 2026


THORChain incident update #1THORChain contributors shared a new update in the dev discord regarding the ongoing incident. TLDR&#8211; Current evidence points toward a newly churned node linked to the attack, likely operated by a single malicious actor&#8211; The leading theory is an…
— THORChain (@THORChain) May 15, 2026


THORChain incident update #2 We have become aware of multiple fake accounts and false information circulating regarding “refunds”, “airdrops”, compensation claims, and other alleged initiatives. To be absolutely clear: &#8211; Initial findings indicate that no user funds were…
— THORChain (@THORChain) May 16, 2026

参考：ザックXBTテレグラムグループ ・ペックシールドアラート（X）・ザ・ブロック 画像：PIXTA
関連ニュース

 2026年4月の暗号資産ハック件数が過去最多に。管理権限侵害やクロスチェーン問題も顕在化
 カーブ創設者、DeFiの安全基準策定を提言。イーサリアム財団とソラナ財団に言及
 ケルプDAO、rsETH不正流出で約2.8億ドル規模の影響。アーベ等にも波及
 DMM Bitcoinの不正流出に北朝鮮ハッカー集団「ラザルス」関与か
北朝鮮系ITワーカーの内部決済データ流出か、390アカウントなど分析結果をZachXBTが公開
