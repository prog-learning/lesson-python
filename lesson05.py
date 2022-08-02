# Scriptを実行 $ python lesson05.py

# リスト（配列）
fruits = ["apple", "banana", "cherry", "durian"]
print(fruits)  # ['apple', 'banana', 'cherry', 'durian']
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # cherry

# 要素を変更
fruits[0] = "orange"
print(fruits)  # ['orange', 'banana', 'cherry', 'durian']

# 要素を最後に追加
fruits.append("grape")
print(fruits)  # ['orange', 'banana', 'cherry', 'durian', 'grape']

# 要素を指定した位置に追加
fruits.insert(1, "lemon")  # 1番目の位置にlemonを追加
print(fruits)  # ['orange', 'lemon', 'banana', 'cherry', 'durian', 'grape']

# 要素を指定して削除
fruits.remove("cherry")  # cherryを削除 見つからない場合はエラー
print(fruits)  # ['orange', 'lemon', 'banana', 'durian', 'grape']

# 最後の要素を削除
fruits.pop()
print(fruits)  # ['orange', 'lemon', 'banana', 'durian']

# 番号を指定して削除
fruits.pop(0)
print(fruits)  # ['lemon', 'banana', 'durian']

# 番号を指定して要素を削除
del fruits[2]
print(fruits)  # ['lemon', 'banana']

# popとdelの違い
r = fruits.pop(1)  # 削除した要素を受け取れる
print(r)  # banana

# 要素を全て削除
fruits.clear()
print(fruits)  # []
