class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요 저는 {self.age}살 {self.name}입니다.")


Person("Alice", 25)
