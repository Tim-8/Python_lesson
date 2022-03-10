# 月を和名で表示する
from datetime import datetime
 
# 月の和名
watuki = ["睦月（むつき）", "如月（きさらぎ）", "弥生（やよい）", "卯月（うづき）", "皐月（さつき）", "水無月（みなづき）", "文月（ふみづき）", "葉月（はづき）", "長月（ながつき）", "神無月（かんなづき）","霜月（しもつき）", "師走（しわす）"]
 
today = datetime.now()  # 現地時刻を取得
 
# 月を取得
month = today.month
 
# 月を和名で表示
print("{}月の和名は、『{}』といいます".format(month, watuki[month-1]))
