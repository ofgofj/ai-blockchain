# ai-blockchain

ブロックチェーン専門のRSS記事収集・分類プロジェクト。プライベートリポジトリ。

## ファイル構成

```
Raw/                 — RSS取得した記事の入口（GitHub Actionsで毎朝自動収集）
Summary/             — 記事生成の出力先
Master/              — トピック別に分類保管（処理済みアーカイブ兼用）
scripts/
  rss_collect.py     — ブロックチェーンRSS収集スクリプト
```

## RSS取得元（全記事取得）

- NFT TIMES: https://nft-times.jp/feed/
- 日本ブロックチェーン協会（JBA）: https://jba-web.jp/feed/
- ガイアックス ブロックチェーン: https://gaiax-blockchain.com/feed/
- ブロックチェーンビジネスコンサルティング: https://blockchain-biz-consulting.com/media/feed/
- あたらしい経済（幻冬舎）: https://www.neweconomy.jp/feed/
- CRYPTO TIMES: https://crypto-times.jp/feed/

## 処理フロー

1. GitHub Actionsで毎朝6:00 JSTにRSS収集 → Raw/に保存
2. 記事生成 → Summary/に出力
3. 処理済み記事をMaster/にトピック別で分類移動
4. Raw/は空になる
