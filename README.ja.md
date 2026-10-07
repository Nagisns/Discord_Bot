# Discord Bot

Pythonと `discord.py` を使用して作成したシンプルなDiscord Botです。このプロジェクトは、PythonとDiscord Bot開発を練習するための学習プロジェクトとして作成しました。

## 機能

- **Ping:** Botのレイテンシ（遅延）をミリ秒単位で表示します。
- **Luck:** 1から100までのランダムな運勢スコアを生成し、結果を表示します。
  - 70～100: `Good luck!`
  - 40～69: `Average luck.`
  - 1～39: `Bad luck...`
- **Guess the Number:** Botが1から100までの数字を1つ選び、その数字を当てるゲームを開始します。ゲームを開始したユーザーのみが回答でき、各チャンネルで同時に実行できるゲームは1つだけです。

## コマンド

| コマンド | 説明 |
|---|---|
| `::ping` | Botのレイテンシをミリ秒単位で表示します。 |
| `::help` | Botのコマンド一覧をEmbed形式で表示します。 |
| `::luck` | ランダムな運勢スコアを生成して結果を表示します。 |
| `::guess` | 数字当てゲームを開始します。 |

存在しないコマンドが入力された場合、そのコマンドが存在しないことを知らせるメッセージを返します。

## 必要環境

- Python 3.10以降
- Discord Botアプリケーション
- `discord.py`
- `python-dotenv`

## セットアップ

### 1. リポジトリをクローンする

```bash
git clone https://github.com/Nagisns/Discord_Bot.git
cd Discord_Bot
```

### 2. 依存パッケージをインストールする

```bash
pip install discord.py python-dotenv
```

### 3. Discord Botを作成・設定する

1. [Discord Developer Portal](https://discord.com/developers/applications) にアクセスします。
2. アプリケーションを作成し、Botを追加します。
3. Botのトークンをコピーします。
4. Botの設定で **Message Content Intent** を有効にします。Botがコマンドメッセージや数字当てゲームの回答を読み取るために、このIntentが必要です。
5. チャンネルの閲覧とメッセージ送信に必要な権限を付与して、Botをサーバーに招待します。

### 4. 環境変数を設定する

プロジェクトディレクトリに `.env` という名前のファイルを作成します。

```env
TOKEN=your_bot_token_here
```

`your_bot_token_here` を自分のBotトークンに置き換えてください。トークンは非公開にし、`.env` をGitにコミットしないでください。

`TOKEN` 環境変数が設定されていない、または空の場合、Botはエラーメッセージを表示して終了します。空白文字だけの値も無効として扱われます。

### 5. Botを起動する

```bash
python src/bot.py
```

Botが起動したら、Botが参加しているサーバー内で各コマンドを使用できます。

## テスト

このプロジェクトでは、単体テストに `pytest` を使用しています。

テストを実行するには、以下のコマンドを使用します。

```bash
python -m pytest
```

現在、`GuessGame` クラスと `ActiveGames` クラスを対象としたテストを実装しています。

## 数字当てゲーム

`::guess` を使用するとゲームが開始します。Botは1から100までの数字を1つ選び、同じチャンネル内でゲームを開始したユーザーからの回答を待ちます。

- 入力した数字が大きすぎる場合、Botは `Too high!` と返信します。
- 入力した数字が小さすぎる場合、Botは `Too low!` と返信します。
- 正解した場合、Botは `Correct!` と返信し、有効な整数を入力した回数を表示します。
- 整数ではないメッセージを入力した場合、有効な整数を入力するよう案内します。この入力は試行回数にはカウントされません。
- 1～100の範囲外の整数を入力した場合、範囲内の数字を入力するよう案内します。この入力も試行回数にはカウントされません。
- Botはプレイヤーからの各メッセージを最大20秒間待ちます。その間にメッセージが送信されなかった場合、ゲームは終了し、Botが正解の数字を表示します。
- 各チャンネルで同時に実行できるゲームは1つだけです。

## ライセンス

このプロジェクトはMIT Licenseのもとでライセンスされています。詳細については [LICENSE](LICENSE) ファイルを参照してください。

## 謝辞

- [discord.py](https://discordpy.readthedocs.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

このREADMEはChatGPTの支援を受けて作成されました。
