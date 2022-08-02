# Scriptを実行 $ python lesson10.py

# class（オブジェクト/構造体の代替）
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):  # 必ずselfを第一引数に入れる
        print(f"Hello! My name is {self.name}.")

    def say_age(self):
        print(f"I'm {self.age} years old.")

    def say_name_and_age(self):
        print(f"My name is {self.name}. I'm {self.age} years old.")

    def say_name_and_age2(self):
        self.say_hello()
        self.say_age()

    def say_calc(self, a, b):
        print(a + b)


taro = Person("Taro", 20)

taro.say_hello()
taro.say_age()
taro.say_name_and_age()
taro.say_name_and_age2()
taro.say_calc(456, 111)
