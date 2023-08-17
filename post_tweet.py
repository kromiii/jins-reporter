import os
import tweepy

def post_tweet(report):
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
  
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)

  # 画像をアップロード
  # with open("report.png", "r") as image_file:
  #   media = client.upload_media(media=image_file.read(), media_category="tweet_image")
  media = api.media_upload('report.png')
  media_id = media.media_id

  # Twitter APIを使ってツイート
  response = client.create_tweet(text=report, media_ids=[media_id])