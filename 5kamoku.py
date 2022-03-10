"""
    学生の5教科テストの得点を入力すると
    各教科の平均点を求めて表示する
    学生の人数を最初に入力させ、
    人数分の5教科テストの得点入力を行う
"""
 
ninzu = 0  # 学生人数
kamoku = ["国語", "算数", "理科", "社会", "英語"]  # 科目名
gokei = [0, 0, 0, 0, 0]  # 科目毎の合計
 
# 学生人数を入力
ninzu = int(input("学生人数？ "))
 
# 学生毎の5教科テスト得点を入力
for i in range(ninzu):  # 人数ループ
    print("{}人目".format(i+1))
    for j in range(5):  # 科目ループ
        print("\t{}の得点 = ".format(kamoku[j]), end="")
        tokuten = int(input())
        # 科目ごとに合計を求める
        gokei[j] += tokuten
 
# 5教科の平均点を表示
print("平均点")
for i in range(5):
    heikin = gokei[i] / ninzu  # 平均 = 合計 ÷ 人数
    print("\t{}: {:.1f}".format(kamoku[i], heikin))
