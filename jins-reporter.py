import os
from fetch_data import fetch_data
from make_report_15s import make_report
from post_tweet import post_tweet

# JINS_TOKEN が設定されていない場合、token.txt が作成されていることを確認
if 'JINS_TOKEN' not in os.environ:
  assert os.path.exists('token.txt'), 'token.txt が存在しません。get_token.py を実行してください。'

# 15秒間隔データの取得
data = fetch_data()
# レポートの作成
report = make_report(data)
# ツイート
post_tweet(report)
# 完了メッセージ
print('レポートの作成が完了しました。')