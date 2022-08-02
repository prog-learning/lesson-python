# Scriptを実行 $ python lesson06.py

# tuple タプル（読み取り専用の配列）
fruits = ("apple", "banana", "cherry")
print(fruits)  # ('apple', 'banana', 'cherry')
print(fruits[1])  # banana


# dict 辞書
fruits = {"apple": 100, "banana": 200, "cherry": 300}
print(fruits)  # {'apple': 100, 'banana': 200, 'cherry': 300}

# キーを指定して値を取得
print(fruits["apple"])  # 100

# キーを指定して値を変更
fruits["apple"] = 500
print(fruits)  # {'apple': 500, 'banana': 200, 'cherry': 300}

# キーを指定して値を削除
del fruits["apple"]
print(fruits)  # {'banana': 200, 'cherry': 300}

# キーを指定して値を追加
fruits["grape"] = 400
print(fruits)  # {'banana': 200, 'cherry': 300, 'grape': 400}

# キーを指定して値が存在するか確認
print("apple" in fruits)  # False
print("banana" in fruits)  # True

# 空をセット
d = {}  # または `dict()` でもOK
print(type(d))
print(d)  # {}


# set 集合（重複を許さない, 順序がなく特定の要素を呼び出せないので注意）
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # {'apple', 'banana', 'cherry'}
# print(fruits)

# 要素を追加
fruits.add("grape")
print(fruits)  # {'apple', 'banana', 'cherry', 'grape'}

# 要素を削除
fruits.remove("banana")
print(fruits)  # {'apple', 'cherry', 'grape'}


# 空をセット
s = set()
print(type(s))
print(s)  # set()
