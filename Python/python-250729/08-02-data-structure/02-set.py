# add
# my_set = {"a", "b", "c", 1, 2, 3}
# my_set.add(4)  # 없는 요소면 추가 순서 X
# print(my_set)  # {1, 2, 3, 4, 'b', 'c', 'a'}

# my_set.add(4)  # set은 중복을 허용하지 않기 때문에 동일하면 그대로
# print(my_set)  # {1, 2, 3, 4, 'b', 'c', 'a'}

# # clear
# my_set = {"a", "b", "c", 1, 2, 3}
# my_set.clear()
# print(my_set)  # set() => set는 ()로 표현 못함 => 닥셔너리

# # remove
# my_set = {"a", "b", "c", 1, 2, 3}
# my_set.remove(2)
# print(my_set)
# my_set.remove(10)  # KeyError: 10 => 없으면 에러 발생

## pop 임의의 요소를 제거하거 반환 => random의 의미는 아님(무작위 x) => 자주 나오는 요소가 있음
# my_set = {"a", "b", "c", 1, 2, 3}
# element = my_set.pop()
# print(element)
# print(my_set)

# # discard => 없어도 remove와 다르게 에러가 발생하지 않음
# my_set = {"a", "b", "c", 1, 2, 3}
# my_set.discard(2)
# print(my_set)
# my_set.discard(10)  # 아무것도 출력되지 않음

# # update
# my_set = {"a", "b", "c", 1, 2, 3}
# my_set.update([1, 4, 5])  # set에 다른 iterable 요소 추가 => 풀어서 넣음
# print(my_set)  # {'c', 2, 3, 1, 'b', 4, 5, 'a'}

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

# print(set1.difference(set2))  # {0, 2, 4}
# print(set1.intersection(set2))  # {1, 3}
# print(set1.issubset(set2))  # False
# print(set3.issubset(set1))  # True
# print(set1.issuperset(set2))  # False
# print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9}
