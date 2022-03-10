"""
    コンピュータとじゃんけんをするゲーム
    あいこの場合も考える
"""
 
import random
    
te = ["グー", "チョキ", "パー"]
 
GU = 0
CHOKI = 1
PA = 2
 
DRAW = 0
WIN = 1
LOSE = 2
 
aiko = False
 
def pon():
    return random.randint(0, 2)
 
print("じゃんけん...")
while True:    
    print("\t1:グー 2:チョキ 3:パー >>> ", end="")
    player = int(input())
    player -= 1
    # プレイヤーの手
    if player < 0 or player > 2:
        print("1～3で入力してね！")
        continue
    # コンピュータの手
    cpu = pon()
 
    # 判定
    if player == cpu:
        kekka = DRAW
    elif (player == GU and cpu == CHOKI) or (player == CHOKI and cpu == PA) or (player == PA and cpu == GU):
        kekka = WIN
    else:
        kekka = LOSE
     
    if aiko == True:
        print("\nしょ！")
    else:
        print("\nぽん！")
 
    print("\tあなた: {}\n\tＣＰＵ: {}".format(te[player], te[cpu]))
     
    if kekka == DRAW:
        print("\nあいこで...")
        aiko = True
        continue
    elif kekka == WIN:
        print("\nあなたの勝ち！")
        break
    else:
        print("\nあなたの負け！")
        break
