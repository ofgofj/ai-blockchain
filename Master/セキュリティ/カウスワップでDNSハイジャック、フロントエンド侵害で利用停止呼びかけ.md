---
title: "カウスワップでDNSハイジャック、フロントエンド侵害で利用停止呼びかけ"
source: "https://www.neweconomy.jp/posts/565313"
published: Wed, 15 Apr 2026 04:09:27 +0000
tags:
  - blockchain
---

カウスワップで偽サイト誘導の可能性
イーサリアム（Ethereum）基盤の分散型取引所（DEX）アグリゲーター「カウスワップ（CoW Swap）」を運営するカウDAO（CoW DAO）で、同サービスのフロントエンドに問題が発生していると公式Xで4月15日（日本時間）に発表された。同DAOは、調査が完了するまでカウスワップを使用しないよう呼びかけている。
同DAOによると、今回の問題は4月14日14:54（UTC）に発生したDNSハイジャックによるものだという。DNSハイジャックとは、正規のドメイン名にアクセスしたユーザーを、攻撃者が用意した別のサーバーへ誘導する攻撃手法だ。見た目が正規サイトと似ている場合、ユーザーが気づかずに不正な操作を行ってしまう可能性がある。
これにより、ユーザーがアクセスする公式ドメイン「swap.cow.fi」が攻撃者により改ざんされ、不正なサイトへ誘導される可能性があったとのこと。
同DAOは、今回の事案について、プロトコルのバックエンドおよびAPIには影響は確認されていないと説明している。一方で、予防措置としてプロトコルの機能を一時的に停止したとしている。
また同DAOは、14:54（UTC）以降にカウスワップ上で行ったトークン承認について、すべて取り消すようユーザーに推奨している。トークン承認とは、特定のコントラクトに対して資産の移動権限を付与する操作であり、不正な承認が行われた場合、資産が引き出される可能性がある。
現在、問題となったドメイン「swap.cow.fi」はロックされておりアクセスできない状態だ。同DAOは、代替として「swap.cow.finance」に新たなフロントエンドを展開しており、代替ドメインは安全に利用可能であると伝えている。
また今回のようにプロトコル自体ではなく、フロントエンドが侵害されるケースでは、スマートコントラクトに問題がなくても、ユーザーが不正なトランザクションを承認することで資産が流出するリスクがある。過去にもパンケーキスワップ（PancakeSwap）やコンパウンド（Compound）など複数のDeFiプロジェクトで同様のDNSハイジャック事案が確認されている。

UPDATE: CoW Swap experienced a DNS hijacking at 14:54 UTC (approximately 90 minutes ago). The CoW Protocol backend and APIs were not impacted, but we have paused them temporarily as a precaution. We are now actively working to resolve the situation. Please continue to…
— CoW DAO (@CoWSwap) April 14, 2026


The CoW Swap frontend is back up at https://t.co/428UojJIdq. Make sure you only sign approvals to 0xc92e8bdf79f0507f65a392b0ab4667716bfe0110 (the original GPv2VaultRelayer contract) https://t.co/phQqIbzPAR
— Felix Leupold (@fleupold_) April 14, 2026

画像：PIXTA
関連ニュース

アーベ、ユーザーが取引で50Mドル相当の損失。カウスワップは手数料返金へ
 CompoundとCelerのウェブサイトがハッキング被害、DNSドメイン攻撃を受け
「Galxe」公式サイトにDNS攻撃、約4000万円の不正流出か
 DeFiプラットフォーム「パンケーキスワップ」と「クリーム・ファイナンス」でDNS攻撃発生、現在は復旧
米SEC、DeFiフロントエンドのブローカー登録不要条件を提示
