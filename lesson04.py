# Scriptを実行 $ python3 lesson04.py

# if文
score = int(input("score ? "))
if score > 80:
    print("Great!")
elif score > 60:
    print("Good!")
else:
    print("So So!")

# 条件演算子
print("Great!" if score > 80 else "so so! ..")
