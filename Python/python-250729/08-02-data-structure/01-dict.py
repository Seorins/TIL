# get
person = {"name": "Alice", "age": 25}
print(person.get("name"))  # 키 값 가져오기 => 없으면 None값 반환
print(person.get("age", 30))  # 키 값이 있다면 있는 값 사용
print(person.get("height", 160))  # 만약 키 값이 없다면 default 값 적용
# print(person['country'])  # KeyError: 'country'

# keys
person = {"name": "Alice", "age": 25}
person_keys = person.keys()  # dict_keys(['name', 'age']) => 객체 반환
print(person_keys)
person["country"] = "Korea"
print(person_keys)  # 실시간으로 동기화되는 확인 창(View)

for key in person.keys():
    print(key, end=" ")

# values
person = {"name": "Alice", "age": 25}
print(person.values())  # dict_values(['Alice', 25]) => 객체 반환

for value in person.values():
    print(value, end=" ")


# items
person = {"name": "Alice", "age": 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])

for key, value in person.items():  # tuple로 오기 때문에 바로 언패킹 해줌
    print(key, value)

# pop
person = {"name": "Alice", "age": 25}
print(person.pop("age"))  # 25  => 제거 후 반환
print(person)  # {'name': 'Alice'} => pop 후 제거된 dict
print(person.pop("country", None))  # None => keyerror 원하지 않으면 default 지정
# print(person.pop('country'))  # KeyError: 'country'

# clear
person = {"name": "Alice", "age": 25}
person.clear()
print(person)

# setdefault => get + 추가 => 키 값이 있으면 값을 반환 없다면 딕셔너리에 추가 후 반환
person = {"name": "Alice", "age": 25}
print(person.setdefault("name"))  # 인자 하나도 가능
print(person.setdefault("name", "Tom"))  # 있으면 기존 값 반환
print(person.setdefault("height"))  # default없고 없는 것을 조회하면 None 반환
print(person.setdefault("country", "KOREA"))  # KOREA
print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}


# update => 딕셔너리도 인자로 받고 키워드 인자도 받음
person = {"name": "Alice", "age": 25}
other_person = {"name": "Jane", "country": "KOREA"}

person.update(other_person)  # 없는 값은 추가하고 동일한 기존 값은 갱신함
print(person)  # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}

person.update(age=100, address="SEOUL")
print(person)  # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}
