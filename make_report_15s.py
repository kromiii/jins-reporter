import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from statsmodels.nonparametric.smoothers_lowess import lowess

def make_report(data):
  # data の中身を確認
  if len(data) == 0:
    print('データがありません。')
    return
  # 装着時間（Hour）
  waring_hour = (~data.isl).sum() * 15 / (60 * 60)
  hour = round(waring_hour,1)
  # 歩数
  steps = data.stp.sum()
  # 前後の傾きの平均
  rotate_x = round(data[abs(data.tl_xav) < 50].tl_xav.mean(),1)
  # 左右の傾きの平均
  rotate_y = round(data[abs(data.tl_yav) < 10].tl_yav.mean(),1)
  
  # 時系列プロット
  # date カラムを timestamp 型に変換
  data['date'] = pd.to_datetime(data['date']) + pd.Timedelta('09:00:00')
  # 複数のカラムに対してLoess平滑化を適用
  columns_to_smooth = ["sc_slp", "sc_fcs", "sc_tsn", "sc_clm"]
  labels = ["awakeness", "concentration", "tension", "calmness"]
  smoothed_data = {}

  for col in columns_to_smooth:
    smoothed_data[col] = lowess(data[col], data['date'], frac=0.1)

  # 覚醒スコアのみ逆数をとる
  smoothed_data["sc_slp"][:, 1] = 100 - smoothed_data["sc_slp"][:, 1]

  # 各カラムのLoessで平滑化されたデータをプロット
  plt.figure(figsize=(8, 6))

  # 他のカラムのLoessで平滑化されたデータ
  colors = ['blue', 'green', 'purple', 'orange']
  for idx, col in enumerate(columns_to_smooth):
    smoothed_dates = pd.to_datetime(smoothed_data[col][:, 0])
    plt.plot(smoothed_dates, smoothed_data[col][:, 1], label=f'{labels[idx]}', color=colors[idx])
  ax = plt.gca()
  ax.xaxis.set_major_locator(dates.HourLocator(interval=1))   # every 4 hours
  ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))  # hours and minutes

  plt.xlabel('Time')
  plt.ylabel('Score')
  plt.title('Time Series Plot with Loess Smoothing for Computed Variables')
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.legend()
  plt.grid(True)
  plt.savefig("report.png")

  # レポートの作成
  report = f"""
  Today's JINS MEME Report
  ================
  装着時間：{hour}時間
  歩数：{steps}歩
  前後の傾きの平均：{rotate_x}度
  左右の傾きの平均：{rotate_y}度
  """
  return report