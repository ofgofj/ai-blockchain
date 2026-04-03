---
title: "仮想通貨約450億円が一瞬で流出？DeFiセキュリティの穴とは"
source: "https://crypto-times.jp/news-drift-hacking-reason/"
published: Fri, 03 Apr 2026 06:28:43 +0000
tags:
  - blockchain
---

Solana（ソラナ）基盤の分散型取引所（DEX）「Drift Protocol」が約2億8,500万ドル（約450億円相当）規模の不正流出被害を受け、DeFiプロジェクトのセキュリティ体制に改めて厳しい視線が注がれています。

Driftは公式Xアカウントで悪意ある攻撃者が「高度なソーシャルエンジニアリング」を含む「新種の攻撃手法（novel attack）」を用いて、プロトコルのセキュリティ・カウンシルに対する管理権限を不正に取得したと発表。攻撃者はフェイクの仮想通貨をDEX上に導入した後、その価格を人為的に吊り上げ借入メカニズムを悪用することで実際の流動性を短時間で抜き取ったとされています。

Earlier today, a malicious actor gained unauthorized access to Drift Protocol through a novel attack involving durable nonces, resulting in a rapid takeover of Drift’s Security Council administrative powers.

This was a highly sophisticated operation that appears to have involved…

— Drift (@DriftProtocol) April 2, 2026

今回の攻撃で焦点となっているのが、Driftが採用するマルチシグウォレットの構造です。攻撃者はわずか2つの秘密鍵の署名を取得しただけでプロトコル全体に対する広範な権限を掌握しました。

ブロックチェーン調査企業Ellipticは報告書の中で攻撃者のオンチェーン上の行動パターンや資金洗浄手法、ネットワークレベルの指標から、北朝鮮（DPRK）との関連を示す兆候があると指摘。専門家や企業によって北朝鮮の関与への見解は割れている状況です。

(adsbygoogle = window.adsbygoogle || []).push({});

専門家の間では対策として「タイムロック」機能の導入が議論されています。タイムロックとは資産のリスティングや出金上限の変更といった重要な操作にあらかじめ時間的な遅延を設けることで異常を検知した際に介入する猶予を確保する仕組みです。

Neoブロックチェーンの創設者であるダン・ホンフェイ氏は数億ドル規模の資金を保有するプロトコルが「数秒で全額流出可能」な状態であってはならないと強調しました。

The Drift exploit exposes a fundamental issue:

Insufficient security around administrative privileges.

If early reports of compromised admin keys or signer authority are accurate, then the first point of failure lies in the fragility of the permission model itself. For… https://t.co/HAPeRiUiZq

— Da Hongfei (@dahongfei) April 2, 2026

一方でタイムロックは対応時間の確保には有効なものの、根本的な原因は特権鍵の侵害でありそれ自体は別の問題であるとの指摘も一部専門家からなされています。

今回のDriftの事例はスマートコントラクトのコード監査だけでは不十分であり、運用面でのリスク管理やガバナンス体制の構築がいかに重要であるかを業界全体に突きつけていると言えます。

Triaカードは世界中で使える仮想通貨クレジットカード (約3000円〜) で、最大6%が仮想通貨でキャッシュバックされます。

仮想通貨での資産運用もカード管理アプリから行えます。早期利用者にはさらなる報酬も用意されているため是非この機会に登録しておきましょう。（登録に必要なアクセスコード：MWVJXJ6475）

©Crypto Times. All rights reserved.
