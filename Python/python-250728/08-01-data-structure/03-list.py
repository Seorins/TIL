# append
my_list = [1, 2, 3]
my_list.append(4) 
print(my_list)  # [1, 2, 3, 4]
# append는 None을 반환합니다.
print(my_list.append(5))  # None

# my_list.append(4, 5, 6) # 여러개는 안됨
# print(my_list)

my_list.append([4, 5, 6]) # iterable 객체는 가능 -> 풀어서 넣진 않음
print(my_list)

# extend iterable한 객체를 넣을 수 있음
my_list = [1, 2, 3]
my_list.extend([4, 5, 6]) # 풀어서 4, 5, 6은 못 넣음 
print(my_list)  # [1, 2, 3, 4, 5, 6]

# extend와 append의 비교
my_list.append([5, 6, 7])
print(my_list)  # [1, 2, 3, 4, 5, 6, [5, 6, 7]]

# my_list.extend(100)  # TypeError: 'int' object is not iterable

# insert
my_list = [1, 2, 3]
my_list.insert(1, 5) # 넣을 자리, 넣을 데이터
print(my_list)  # [1, 5, 2, 3]

# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2) # 동일한 첫번째 데이터만 제거
print(my_list)  # [1, 3, 2, 2, 2]

# pop 리스트에서 지정한 인덱스의 항목을 제거하고 반환 작성하지 않으면 마지막 거 제거 
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4] => 원본 변형


# clear 요소만 제거함, list 제거 x
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []

# index 해당 데이터의 인덱스를 반환 
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1

# count 해당 데이터의 개수를 반환
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3

# reverse 역순으로 뒤집음 (정렬x)
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
# reverse는 None을 반환합니다.
# print(my_list.reverse())  # None
# reverse는 원본 리스트를 변경합니다.
print(my_list)  # [9, 1, 8, 2, 3, 1]

# sort default = 오름차순
my_list = [3, 2, 100, 1]
my_list.sort()
# sort는 None을 반환합니다.
# print(my_list.sort())  # None
# sort는 원본 리스트를 변경합니다.
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]
