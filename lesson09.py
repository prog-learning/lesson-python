# Scriptを実行 $ python lesson09.py

# 関数
def say_hello():
    print("Hello!")


# 実行
say_hello()

# 引数
def say_hi(name="no_name", age=0):  # デフォルト引数
    print(f"Hi! {name}({age})")


# 呼び出し
say_hi("tom", 23)  # tom(23)
say_hi("bob")  # ageはデフォルト引数の0が入る
say_hi(age=25, name="Ken")  # キーワード引数


# 戻り値
def add(a, b):
    return a + b


print(add(1, 2))  # 3
result = add(2, 3)

print(result)  # 5
