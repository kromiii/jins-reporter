import pandas as pd

def make_report(data):
  # data の中身を確認
  if len(data) == 0:
    print('データがありません。')
    return
  # 装着時間（Hour）
  hour = round(data.wea_s.sum() / (60*60),1)
  # 歩数
  steps = data.stp_fst.sum() + data.stp_mid.sum() + data.stp_slw.sum() + data.stp_vsl.sum()
  # 前後の傾きの平均
  rotate_x = round(data[abs(data.tl_xav) < 50].tl_xav.mean(),1)
  # 左右の傾きの平均
  rotate_y = round(data[abs(data.tl_yav) < 10].tl_yav.mean(),1)
  # 瞬き間隔平均
  blick = round(data.sc_bki_av.mean(),1)

  # レポートの作成
  report = f"""
  Today's JINS MEME Report
  ================
  装着時間：{hour}時間
  歩数：{steps}歩
  前後の傾きの平均：{rotate_x}度
  左右の傾きの平均：{rotate_y}度
  瞬き間隔平均：{blick}秒
  """
  print(report)

  # Twitter APIを使ってツイート
  import os
  import tweepy

  # Twitter API 固有値
  consumer_key = os.environ['TWITTER_CONSUMER_KEY']
  consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
  access_token = os.environ['TWITTER_ACCESS_TOKEN']
  access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

  # Twitter APIの認証
  client = tweepy.Client(
      consumer_key=consumer_key, consumer_secret=consumer_secret,
      access_token=access_token, access_token_secret=access_token_secret
  )
  # Twitter APIを使ってツイート

  client.create_tweet(text=report)

