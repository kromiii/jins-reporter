import os
from fetch_data import fetch_data
from make_report import make_report

# JINS_TOKEN が設定されていない場合、token.txt が作成されていることを確認
if 'JINS_TOKEN' not in os.environ:
  assert os.path.exists('token.txt'), 'token.txt が存在しません。get_token.py を実行してください。'

# 60秒間隔データの取得
data = fetch_data()
# レポートの作成
make_report(data)
# 完了メッセージ
print('レポートの作成が完了しました。')