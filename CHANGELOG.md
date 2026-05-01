# ai-blockchain 変更ログ

プロジェクトの運用・スキル・設定の変更履歴を記録する。コード差分はgit logを参照。

---

## 2026-04-24

### 新規: `bc-notebooklm-audio` スキル作成
- 場所: `.claude/skills/bc-notebooklm-audio/SKILL.md`
- 内容: 当日のSummary MDをNotebookLMに登録し、音声概要（Audio Overview / podcast）を生成するスキル
- 参考元: ai_catchup側の`my-notebooklm-generate`（スライド生成版）を音声版に改造
- 当日の音声は生成成功（Notebook ID: `13c2f828-677e-41b0-a806-7395fe7b821c` / タイトル自動生成「Googleが破るサトシの10兆円」/ 生成時間 約13分）

### スキル運用方針の確定
- **一気通貫フロー**: `blockchain-catchup` → `bc-notebooklm-audio` の2ステップで毎日の作業が完結
- **git push は行わない**: 音声URL保存による `Summary/` 追加コミットはchat-notify.ymlを二重発火させてGoogle Chat通知が2回飛ぶため。URL txtはローカル参照用として未追跡のまま残す運用
- **アカウント分離は断念**: notebooklm-pyがbrowser_profileを共有するため、`--storage`指定でのマルチアカウント運用は実用的でないと判断。zept.designアカウントで統一

### プロンプトの大幅書き換え（完全初心者向けに）
- `bc-notebooklm-audio` のSTEP 5プロンプトを、ブロックチェーン・ビットコイン・暗号資産の知識がゼロの人（高校生レベル）でも理解できる内容に全書き換え
- 全専門用語を毎回一から解説するルール（「〜はご存知の通り」などの暗黙の前提を禁止）
- 2人のホストの「素朴な質問役 × 解説役」の掛け合い形式を指定
- 投資助言にならないよう断定口調を禁止

### Chatwork通知の自動化
- 生成成功後、Chatworkルーム **`376976342`** に**URL1行だけ**を自動送信するSTEP 8を追加
- 送信形式: `https://notebooklm.google.com/notebook/XXX` のみ（日付・装飾なし）
- 実装: Node.js + httpsモジュール（curlは文字化けリスクあり）
- APIトークンは `~/.bashrc` の `CHATWORK_API_TOKEN` から取得（bashで `source` して子プロセスに渡す）
- 当日テスト送信成功（`message_id: 2099515507580604416`）

---
