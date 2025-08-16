# # 정수
# # 정수는 계속 동일한 위치를 씀 => 동일한 결과가 나옴
# # 정수 => 해시 함수 => 정수 (따라서 지연평가와 같이 게으름 발생)
# my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set)

# # 문자열
# # 문자열 => 해시함수(난수화 진행) => 정수
# my_str_set = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
# print(my_str_set.pop())
# print(my_str_set.pop())
# print(my_str_set.pop())
# print(my_str_set.pop())
# print(my_str_set.pop())

print(hash(1))
print(hash(1))
print(hash("a"))
print(hash("a"))

# print(hash(1))
# print(hash(1.0))
# print(hash('1'))
# print(hash((1, 2, 3)))

# TypeError: unhashable type: 'list'
# print(hash((1, 2, [3, 4])))
# TypeError: unhashable type: 'list'
# print(hash([1, 2, 3]))
# TypeError: unhashable type: 'list'
# my_set = {[1, 2, 3], 1, 2, 3, 4, 5}
# TypeError: unhashable type: 'set'
# my_dict = {{3, 2}: 'a'}
