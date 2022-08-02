# Scriptを実行 $ python lesson08.py

# 繰り返し処理

# while文
i = 0
name = "Taro"

while i < 6:
    # if i == 3:
    #     break # iが3の時にループを抜ける
    print(f"while文:{i}")
    i += 1
else:
    print("finish!")  # breakしない場合のみ実行


# for文1
for i in range(5):
    print(f"for文:{i}")

# for文2
for i in range(0, 8):  # 0から7まで
    # for i in range(0, 10, 2):  # 0から9まで2ずつ
    if i == 4:
        # break  # iが4の時にループを抜ける
        continue  # iが4の時にスキップする
    print(i)
# 終了後の処理
else:
    print("Finish!")

# for文3
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
