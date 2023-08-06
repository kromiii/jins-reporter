# jins-reporter

## Overview
JINS-API に接続して JINS MEME のデータを取得し Twitter に投稿するプログラムです
Github Action を設定することで定期的に実行することができます

レポートに含まれる指標は以下の通りです
* 装着時間：JINS MEME を装着していた時間
* 歩数：JINS MEME を装着していた時間における歩数
* 頭部の傾き（前後）：頭部の傾き（縦） 値が大きいほど前傾姿勢
* 頭部の傾き（左右）：頭部の傾き（横） 値が大きいほど右傾姿勢
* まばたき間隔（秒）：まばたき間隔（秒） 長すぎるとドライアイの可能性あり

## Usage

JINS API トークンを取得するための環境変数を設定

```bash
$ export JINS_CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export JINS_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

JINS API を使うためのトークンを取得
```bash
$ python get_token.py
```

ブラウザが起動するので、JINS MEME のアカウントでログインして遷移先のURLをコピーして、ターミナルに貼り付けて Enter を押す

token.txt が生成されます

生成されたトークンは３０日間有効です

Twitter に投稿するための環境変数を設定

```bash
$ export TWITTER_CONSUMER_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export TWITTER_CONSUMER_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export TWITTER_ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export TWITTER_ACCESS_TOKEN_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

実行

```bash
$ python jins-reporter.py
```

レポートが生成され、Twitter に投稿されます

## Github Action
Github Action を使う場合は token.txt の内容を Github の Secrets に登録してください

```
JINS_TOKEN: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
