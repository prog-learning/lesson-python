# Scriptを実行 $ python3 lesson05.py

# while文
i = 0
name = "Taro"

while i < 10:
    if i == 5:
        break
    print("{0:}:{1:}".format(i, name))
    print("%d:%s" % (i, name))
    i += 1
else:
    print("finish!")


# for文
for i in range(0, 10):
    if i == 5:
        # break
        # iが5の時にスキップする。
        continue
    print(i)
# 終了後の処理
else:
    print("Finish!")
