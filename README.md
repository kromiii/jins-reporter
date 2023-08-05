# jins-reporter

## Overview
JINS-API に接続して JINS MEME のデータを取得し Twitter に投稿するプログラムです

## Description
プログラムを実行すると当日のJINS MEMEのデータを取得し、下記の指標を計算した上で、指定した Twitter アカウントに投稿します

レポートに含まれる指標は以下の通りです
* 装着時間：JINS MEME を装着していた時間
* 歩数：JINS MEME を装着していた時間における歩数
* 頭部の傾き（左右）：JINS MEME を装着していた時間における頭部の傾き（横）
* 頭部の傾き（前後）：JINS MEME を装着していた時間における頭部の傾き（縦）
* まばたき間隔（秒）：JINS MEME を装着していた時間におけるまばたき間隔（秒）

## Usage

環境変数を設定

```bash
$ export JINS_CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export JINS_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export
TWITTER_CONSUMER_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export TWITTER_CONSUMER_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export TWITTER_ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export TWITTER_ACCESS_TOKEN_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

JINS API を使うためのトークンを取得
```bash
$ python get_token.py
```

ブラウザが起動するので、JINS MEME のアカウントでログインして遷移先のURLをコピーして、ターミナルに貼り付けて Enter を押す

token.txt が生成されます

生成されたトークンは３０日間有効です

実行

```bash
$ jins-reporter
```

定期的に実行する場合は cron を利用します

```bash
$ crontab -e
```

```bash
*/5 * * * * /path/to/jins-reporter
```