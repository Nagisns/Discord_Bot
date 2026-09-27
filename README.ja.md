# Discord Bot

Python と `discord.py` で作成したシンプルな Discord Bot です。Python と Discord Bot の開発を学ぶためのプロジェクトです。

## 機能

- **Ping：** Bot のレイテンシ（応答速度）をミリ秒単位で表示します。
- **Luck：** 1〜100 のランダムな運勢スコアを生成し、結果を表示します。
  - 70〜100：`Good luck!`
  - 40〜69：`Average luck.`
  - 1〜39：`Bad luck...`
- **数字当てゲーム：** Bot が1〜100の数字を選び、その数字を当てるゲームを開始します。回答できるのはゲームを開始したユーザーだけです。また、同じチャンネルで同時に実行できるゲームは1つだけです。

## コマンド

| コマンド | 説明 |
|---|---|
| `::ping` | Bot のレイテンシをミリ秒単位で表示します。 |
| `::luck` | ランダムな運勢スコアを生成して表示します。 |
| `::guess` | 数字当てゲームを開始します。 |

存在しないコマンドを入力すると、そのコマンドが存在しないことを知らせるメッセージが返ります。

## 必要なもの

- Python 3.10 以降
- Discord Bot アプリケーション
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

### 3. Discord Bot を作成して設定する

1. [Discord Developer Portal](https://discord.com/developers/applications) を開きます。
2. アプリケーションを作成し、Bot を追加します。
3. Bot のトークンをコピーします。
4. Bot の設定で **Message Content Intent（メッセージコンテンツインテント）** を有効にします。このインテントは、Bot がコマンドや回答のメッセージを読み取るために必要です。
5. チャンネルの閲覧とメッセージの送信ができる権限を付与して、Bot をサーバーに招待します。

### 4. 環境変数を設定する

プロジェクトのディレクトリに `.env` という名前のファイルを作成します。

```env
TOKEN=your_bot_token_here
```

`your_bot_token_here` を実際の Bot トークンに置き換えてください。トークンは他人に共有せず、`.env` を Git にコミットしないでください。

### 5. Bot を起動する

```bash
python bot.py
```

Bot が起動したら、Bot が参加しているサーバーでコマンドを使えます。

## 数字当てゲームの遊び方

`::guess` を入力するとゲームが始まります。Bot が1〜100の数字を選び、ゲームを開始したユーザーから同じチャンネル内で回答が届くのを待ちます。

- 数字が正解より大きい場合、Bot は `Too high!` と返信します。
- 数字が正解より小さい場合、Bot は `Too low!` と返信します。
- 正解すると、Bot は `Correct!` と返信し、有効な整数で回答した回数を表示します。
- 整数以外のメッセージには、有効な整数を入力するよう案内します。このメッセージは回答回数に含まれません。
- Bot は回答者からのメッセージを最大20秒待ちます。時間内にメッセージが届かない場合、ゲームは終了し、正解の数字が表示されます。
- 同じチャンネルで同時に実行できるゲームは1つだけです。

## ライセンス

このプロジェクトは MIT License のもとで公開されています。詳しくは [LICENSE](LICENSE) ファイルを確認してください。

## 謝辞

- [discord.py](https://discordpy.readthedocs.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

この README の作成には ChatGPT の支援を受けました。
