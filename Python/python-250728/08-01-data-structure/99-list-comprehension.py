# 사용 전
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)


# 사용 후
number_list = [x**2 for x in numbers]
# number_list = list(x**2 for x in numbers)
print(number_list)

# List Comprehension 활용 예시
# "2차원 배열 생성 시 (인접행렬 생성 시)"

data = [[0] * 5 for _ in range (5)]
data2 = [[0 for _ in range(5)] for _ in range(5)]

print(data)
print(data2)
"""
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
"""
