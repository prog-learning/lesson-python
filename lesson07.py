# Scriptを実行 $ python lesson07.py

score = 55  # inputで入力できる 文字列なのでintに変換

# if文
if score > 80:
    print("Great!")
elif score > 60:
    print("Good!")
else:
    print("So So!")

# 1行で書く場合
print("Great!" if score > 80 else "so so! ..")


# じゃんけんゲーム

# 0:グー 1:チョキ 2:パー
handNum = int(input("じゃんけんをします。0:グー、1:チョキ、2:パーのいずれかの数字を入力してください。"))

# じゃんけんの手
hands = ["グー", "チョキ", "パー"]

# コンピュータの手
import random

computerHand = random.randint(0, 2)

# 勝敗
if handNum == computerHand:
    print("あいこ😐")
elif handNum == 0 and computerHand == 1:
    print("勝ち🎉")
elif handNum == 1 and computerHand == 2:
    print("勝ち🎉")
elif handNum == 2 and computerHand == 0:
    print("勝ち🎉")
else:
    print("負け💀")

print("あなたの手は{0}、コンピュータの手は{1}です。".format(hands[handNum], hands[computerHand]))
