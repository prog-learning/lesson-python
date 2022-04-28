# Scriptを実行 $ python3 lesson06.py

# 関数
def say_hi(age, name="no_name"):
    print("Hi! {0} age({1})".format(name, age))


# 呼び出し
say_hi("tom", 23)
say_hi("Bob", 24)

# 戻り値
def add(a, b):
    return a + b


add(1, 2)
