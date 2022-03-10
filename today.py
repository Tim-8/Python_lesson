# 今日の日付と日時を表示する
from datetime import datetime
 
# 曜日を漢字で表示するため（0 → 月曜日... 6 → 日曜日）
youbi = ["月", "火", "水", "木", "金", "土", "日"]
 
today = datetime.now()  # 現地時間を取得
 
# 年月日
year = today.year
month = today.month
day = today.day
 
# 曜日を0～6で取得（0が月曜日）
weekday = today.weekday()
 
# 時分秒
hour = today.hour
minute = today.minute
second = today.second
 
# 表示
print("{}年{}月{}日（{}）".format(year, month, day, youbi[weekday]))
print("{}時{}分{}秒".format(hour, minute, second))
