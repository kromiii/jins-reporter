import urllib.request
import json
import pandas as pd

#JINS MEME API 固有値
summarydata_url = 'https://apis.jins.com/meme/v2/users/me/official/standard_mode_logs'

#データ取得レンジ、1日以内をセットしてください
params = {
    'date_from': '2023-08-04T00:00:00+09:00',
    'date_to': '2023-08-04T23:59:59+09:00',
}

"""
60秒データの取得とCSV保存
"""
#結合・格納先dataframe
data_60s_interval_df = pd.DataFrame()

#1レスポンスのデータをdata_60s_interval_dfに追記する関数
def concat_60s_interval_data(res_data):
    #時間帯毎に属性が分かれるので、それぞれの時間帯をたどる
    for hour in res_data["standard_mode_logs"]:
        tmp_df = pd.DataFrame(res_data["standard_mode_logs"][hour])
        print("hour:" + hour + " len:" + str(len(tmp_df))) #統計情報の表示

        # グローバルのdfにconcatする
        global data_60s_interval_df
        data_60s_interval_df = pd.concat([data_60s_interval_df, tmp_df])

#60秒間隔データのリクエスト
def get_60s_interval_data(url, headers, cursor=None):
    #cursorがセットされている時はURLパラメターに追記する
    final_url = url + ("" if cursor is None else "&cursor=" + cursor)
    req = urllib.request.Request(final_url, headers=headers)
    with urllib.request.urlopen(req) as res:
        #レスポンスのparse
        raw = json.load(res)

        #dataをくっつける
        concat_60s_interval_data(raw)

        #cursorがセットされていた場合、再帰でデータをリクエストする
        if raw["cursor"] is not None:
            print("cursor: " + raw["cursor"])
            get_60s_interval_data(url, headers, cursor=raw["cursor"])
        else:
            print("cursor none, fetch end")

#取得の実行
#60秒間隔データのリクエストの作成
url = summarydata_url + '?' + urllib.parse.urlencode(params)
# トークンの読み込み
with open('token.txt', 'r') as f:
    access_token = f.read()
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Accept': 'application/json'
}

get_60s_interval_data(url, headers)
#print(data_60s_interval_df.info())

#取得データの保存
data_60s_interval_df.to_csv('60s_interval_data.csv', index=False)


