# 문자열 표현
print('Hello, World!')  # Hello, World!
print(type('Hello, World!'))  # str

# 중첩 따옴표
print(
    '문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.'
)  # 문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.
print(
    "문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다."
)  # 문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.

# Escape sequence
# 따옴표 앞에 \를 붙여 문자로 인식시킴
print('He\'s a boy.')
# \n 은 줄바꿈(엔터)을 의미함
print('첫째 줄\n둘째 줄')

# 여러 줄 문자열을 작성할 때는 """ 또는 '''를 사용
multi_line_str = """
이것은
여러 줄로 이루어진
문자열입니다.
"""
print(multi_line_str)


# String Interpolation "f-string"
'''
f-string은 줄이 실행될 때 name과 age의 현재 값을 문자열 안에 바로 넣어버림
따라서 후에 name과 age의 값이 바뀌어도
greeting 문자열은 원래 시점의 값을 반영하게 됨
'''

name = '홍길동'
age = 25
greeting = f'안녕하세요, 제 이름은 {name}이고 나이는 {age}살입니다.'
# 안녕하세요, 제 이름은 홍길동이고 나이는 25살입니다.
print(greeting)

# 따라서 f-string은 그때그때 새로 생성해야 함
name = '김싸피'
age = 30
greeting = f'안녕하세요, 제 이름은 {name}이고 나이는 {age}살입니다.'
print(greeting)




# 문자열의 시퀀스 특징
my_str = 'hello'
# 1. 인덱싱
print(my_str[1])  # e


# 2. 슬라이싱
print(my_str[2:4])  # ll
print(my_str[:3])  # hel
print(my_str[3:])  # lo
print(my_str[::2])  # hlo
print(my_str[::-1])  # olleh

print(my_str[-1:-3])  #출력 안됨 작은 것 ~ 큰 것 (순서 정방향 => 1이 생략된 것)
print(my_str[-3:-1]) #출력 ll
print(my_str[-1:-3:-1]) #출력 ol

# 3. 길이
print(len(my_str))  # 5

# 4. 문자열은 불변
# TypeError: 'str' object does not support item assignment
# my_str[1] = 'z'
