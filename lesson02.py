# Scriptを実行 $ python3 lesson02.py

# 変数
message = "やっほー"
print(message)

message = "yahoo"
print(message)


# 定数
MESSAGE = "ﾔﾎｰ"
print(MESSAGE)

# 大文字にした場合は定数にしようみたいな慣習があるが、エラーにはならず普通に書き換わる
MESSAGE = "yahoo"
print(MESSAGE)


# 変数の埋め込み
name = "nob"
score = 31.6
print("name:{0} score:{1}".format(name,score))