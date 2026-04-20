---
title: "サークル、USDCのクロスチェーン転送基盤「USDC Bridge」提供開始"
source: "https://www.neweconomy.jp/posts/566483"
published: Mon, 20 Apr 2026 07:28:18 +0000
tags:
  - blockchain
---

サークルがラップ不要のUSDC転送基盤を提供開始
米ドル連動型ステーブルコイン「USDC」の発行元サークル（Circle）が、USDCを複数のブロックチェーン間で移動するための新機能「USDCブリッジ（USDC Bridge）」の提供開始を4月17日に発表した。なお記事執筆時点で専用のインターフェースも公開されている。
サークルの発表によると同機能は、サークル提供のクロスチェーン転送基盤「クロスチェーントランスファープロトコル（Cross-Chain Transfer Protocol：CCTP）」を基盤とした公式のブリッジ機能。ネイティブなUSDCをチェーン間で移動するための標準的な手段として提供されるものだという。
同社によるとUSDCブリッジでは、従来のブリッジで用いられてきたラップド資産や合成資産ではなく、ネイティブUSDCそのものを転送できる点が特徴とされている。同機能では、送信元チェーンでUSDCを焼却（バーン）し、送信先チェーンで新たに発行（ミント）する1対1の方式が採用されている。
また同機能では、手数料が事前に表示されるほか、送金の進行状況をリアルタイムで確認できる仕組みが提供されている。さらに、送信先チェーンにおけるガス代の処理も自動で行われるなど、従来のブリッジに伴う操作の複雑さを軽減する設計が特徴だ。
対応チェーンについては、イーサリアム（Ethereum）やアバランチ（Avalanche）、アービトラム（Arbitrum）、ベース（Base）、ポリゴン（Polygon）など、イーサリアム仮想マシン（EVM）互換チェーン間での転送に対応するとのこと。
なおCCTP自体はソラナ（Solana）やアプトス（Aptos）など非EVM系チェーンにも対応しているが、USDCブリッジとしての提供は現時点でEVM互換チェーンのみの対象となる。
また同社はあわせて、開発者向け機能「サークル・ゲートウェイ（Circle Gateway）」において、ソラナへのクロスチェーン転送対応開始を発表している。同機能は、送金先チェーンでの処理自動化により、クロスチェーン送金の運用負荷の軽減を図るものとされる。

Introducing the USDC Bridge.A direct way to move USDC crosschain.Built and operated by Circle, USDC Bridge gives you a predictable, transparent way to move USDC between chains:→ Native burn-and-mint transfers→ Clear fees upfront, with live status and progress→ No route… pic.twitter.com/EZUFJhzX8U
— USDC (@USDC) April 17, 2026


Crosschain forwarding to @solana is now live for Circle Gateway.Gateway enables chain-agnostic USDC balances that can be spent in &lt;500 ms crosschain, or programmatically batched to facilitate sub-cent agentic nanopayments.Circle’s forwarding service automates… pic.twitter.com/j31fMQfTwO
— Circle (@circle) April 17, 2026

参考：USDCブリッジ画像：PIXTA
関連ニュース

イーサリアム上の決済ネットワーク「Morph」、ネイティブUSDCとCCTP導入へ
Circleの「CCTP」がアップグレード、「USDC」クロスチェーン転送時間を短縮
サークル「CCTP」がSuiに対応、9チェーン間で「USDC」のネイティブ送信可能に
チェーンリンク「CCIP」がサークル「CCTP」と統合、クロスチェーンアプリで「USDC」利用可能
サークルがDEX「edgeX」に戦略投資、エッジチェーンにネイティブUSDCとCCTP導入へ
