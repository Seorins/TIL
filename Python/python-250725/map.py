# 언패킹
# map(함수, 반복가능한 자료형 )
one, two, three = list(map(int, input().split()))
print(one, two, three)

# 1 
input_num = list(map(int, input().split()))
print(input_num)

# 2
words = ['apple', 'banana', 'kiwi']
words_len = list((map(len, words)))
print(words_len)


# 3
nums = [1, 2, 3, 4, 5]
words_two = list(map(lambda x : x ** 2, nums))
print(words_two)

# 4
# x.upper() 가능
words2 = ['apple', 'banana', 'kiwi']
upper_words = list(map(lambda x : str.upper(x), words2))
print(upper_words)

# 5
def my_map(func, iterable):
    ls = []
    for i in iterable :
        res = func(i)
        ls.append(res)
    return ls
        

result = my_map(lambda x: x * 2, [1, 2, 3, 4])
print(list(result))  # [2, 4, 6, 8]

# 6 
a = [1, 2, 3]
b = [10, 20, 30]

add_list = list(map(lambda x, y : x + y, a, b))
print(add_list)

# list로 표현하고 싶진 않을 땐 변수 앞에 * 붙이면 됨
print(*add_list)



# 둘 다 가능. map은 형변환까지 하고 싶을 때 주로 사용
a, b, c = input().split()

d, e, f = map(str, input().split())

