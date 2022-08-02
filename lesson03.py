# Scriptを実行 $ python lesson03.py

# データ型

# 整数
i = 10
print(type(i))  # <class 'int'>

# 浮動小数点
f = 23.4
print(type(f))  # <class 'float'>

# 文字列
s = "hello"
print(type(s))  # <class 'str'>

# 論理値
b = True
print(type(b))  # <class 'bool'>

# None
n = None
print(type(n))  # <class 'NoneType'>

# リスト
l = [1, 2, 3, 4, 5]
print(type(l))  # <class 'list'>

# タプル
t = (1, 2, 3, 4, 5)
print(type(t))  # <class 'tuple'>

# 辞書
d = {"x": 100, "y": 200}
print(type(d))  # <class 'dict'>

# 集合
st = {1, 2, 3, 4, 5}
print(type(st))  # <class 'set'>

# データ型の変換
tr = int("100")  # 文字列を整数に変換
print(type(tr))  # <class 'int'>
