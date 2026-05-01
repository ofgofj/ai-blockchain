# ai-blockchain 作業ログ

## 2026-04-27

### BCキャッチアップ実行（3日分まとめて処理）
04-25・04-26のキャッチアップをスキップしていたため、Raw/に47件の記事が積み残し状態だった。
- Raw/index.md は当日（04-27）分の15件しか掲載されていなかったが、Raw/*.mdの実ファイルは47件あり過去日分が残存していたことを発見
- 04-24既出の18件を除外、新規29件で詳細解説6本＋一覧18件を構成
- 詳細解説: テザーUSDT凍結／ロシア越境決済法案／メタプラ80億円社債／Bitwarden CLIマルウェア／日本企業BTC積み増し／スタークネットShinobi
- 基礎講座テーマ: ステーブルコインの「凍結機能」って何？
- レポート: Summary/2026/04/2026-04-27.md
- コミット: a7bbf15、Google Chat通知 success

### NotebookLM音声概要生成
- ノートブックID: 0ddf6cd9-a2e1-402d-8678-51eb98a55517
- 共有URL: https://notebooklm.google.com/notebook/0ddf6cd9-a2e1-402d-8678-51eb98a55517
- 保存: Summary/2026/04/2026-04-27-notebooklm-audio-url.txt および -artifact-id.txt（git追跡外）
- Chatworkマイチャット通知 success（HTTP 200, message_id: 2100427721309167616）

### スキル更新（.claude/skills/、git管理外）
**.claude/skills/blockchain-catchup/SKILL.md**
- STEP 1に「複数日分の記事が溜まっている場合の処理」セクションを追加。Raw/index.mdは毎朝上書きされる仕様、Raw/*.mdの実ファイル数で判断、レポート冒頭に「（X日分まとめ）」注記
- STEP 2に「重複判定の実務」セクションを追加。RSS自動収集が同じ記事を再収集するケースを除外件数に「※前回既報含む」と明記する運用

**.claude/skills/bc-notebooklm-audio/SKILL.md**
- STEP 8タイトルに「= ユーザーのマイチャット」を併記
- ルームID 376976342 がChatwork API /v2/me で返る `room_id`（=マイチャット）であることを明記。「マイチャットに送って」と言われても二重送信不要

### 発見事項
- `.claude/` は .gitignore で除外されているため、スキル更新はローカル保存のみで完結（push対象外）
- Chatwork API `/v2/me` で取得できる `room_id` フィールドはユーザーのマイチャットID
