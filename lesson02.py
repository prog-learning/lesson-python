# Scriptを実行 $ python lesson02.py

# 変数
message = "やっほー"
print(message)

message = "yahoo"  # 上書き可能
print(message)


# 定数（大文字で書く）
MESSAGE = "ﾔﾎｰ"
print(MESSAGE)

# 大文字にした場合は定数にしようみたいな慣習があるが、エラーにはならず普通に書き換わる
MESSAGE = "yahoo"
print(MESSAGE)


# 変数の埋め込み
name = "nob"
score = 31
print("{0}さん、{1}点です。".format(name, score))
print(f"{name}さん、{score}点です。")  # ※Python v3.6で追加
