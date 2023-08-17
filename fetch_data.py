import urllib.request
import json
import pandas as pd
import datetime
import os

def fetch_data():
  #JINS MEME API 固有値
  logicdata_url = 'https://apis.jins.com/meme/v2/users/me/official/computed_data'

  #データ取得レンジ
  # 今日の日付を取得
  today = datetime.date.today().strftime("%Y-%m-%d")
  params = {
    'date_from': f'{today}T00:00:00+09:00',
    'date_to': f'{today}T23:59:59+09:00',
  }

  """
  15秒データの取得とCSV保存
  """
  #結合・格納先dataframe
  data_15s_interval_df = pd.DataFrame()

  #1レスポンスのデータをdata_15s_interval_dfに追記する関数
  def concat_15s_interval_data(res_data):
    #時間帯毎に属性が分かれるので、それぞれの時間帯をたどる
    for hour in res_data["computed_data"]:
      tmp_df = pd.DataFrame(res_data["computed_data"][hour])
      print("hour:" + hour + " len:" + str(len(tmp_df))) #統計情報の表示

      # グローバルのdfにconcatする
      nonlocal data_15s_interval_df
      data_15s_interval_df = pd.concat([data_15s_interval_df, tmp_df])
  #15秒間隔データのリクエスト
  def get_15s_interval_data(url, headers, cursor=None):
    #cursorがセットされている時はURLパラメターに追記する
    final_url = url + ("" if cursor is None else "&cursor=" + cursor)
    req = urllib.request.Request(final_url, headers=headers)
    with urllib.request.urlopen(req) as res:
      #レスポンスのparse
      raw = json.load(res)

      #dataをくっつける
      concat_15s_interval_data(raw)

      #cursorがセットされていた場合、再帰でデータをリクエストする
      if raw["cursor"] is not None:
        print("cursor: " + raw["cursor"])
        get_15s_interval_data(url, headers, cursor=raw["cursor"])
      else:
        print("cursor none, fetch end")

  #取得の実行
  #15秒間隔データのリクエストの作成
  url = logicdata_url + '?' + urllib.parse.urlencode(params)
    # トークンの読み込み
  if 'JINS_TOKEN' not in os.environ:
    with open('token.txt', 'r') as f:
      access_token = f.read()
  else:
    access_token = os.environ['JINS_TOKEN']
  #リクエストヘッダーの作成
  headers = {
    'Authorization': 'Bearer ' + access_token,
    'Accept': 'application/json'
  }

  get_15s_interval_data(url, headers)
  #print(data_15s_interval_df.info())

  #取得データの保存
  data_15s_interval_df.to_csv('15s_interval_data.csv', index=False)

  return data_15s_interval_df


