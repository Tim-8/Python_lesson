from datetime import datetime
 
today = datetime.now()
 
# 現在時刻を表示
hour = today.hour
minute = today.minute
print("{}:{}".format(hour, minute))
 
# 時間帯によりメッセージを変えて表示
if hour >= 3 and hour <= 9:
    print("起きてる？")
elif hour >= 10 and hour <= 17:
    print("こんちわ！")
elif hour >= 18 and hour <=21:
    print("お晩です")
else:  # 夜10時から真夜中の2時
    print("夜分遅くにすいません")