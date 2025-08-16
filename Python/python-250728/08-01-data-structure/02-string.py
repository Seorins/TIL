# find
text = 'banana'
print(text.find('a'))  # 있으면 1
print(text.find('z'))  # 없으면 -1
print('------------------------------')

# index
print(text.index('a'))  # 1 해당 문자가 어느 위치에 있는지 반환 (젤 처음 거)
# print(text.index('z'))  # ValueError: substring not found 
print('------------------------------')

# isupper 모든 문자가 대문자인지
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # True
print(string2.isupper())  # False
print('------------------------------')

# islower 모든 문자가 소문자인지
print(string1.islower())  # False
print(string2.islower())  # False
print('------------------------------')

# isalpha 모든 문자가 알파벳인지 
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # True
print(string2.isalpha())  # False
print('------------------------------')

# replace
text = 'Hello, world! world world'
new_text1 = text
new_text2 = text
print(new_text1.replace('world', 'python'))  # Hello, Python! Python Python
print(new_text2.replace('world', 'python', 1))  # Hello, Python! world world
print('------------------------------')

# strip 공백 제거
text = '  Hello, world!  '
new_text = text
print(new_text.strip('Hello'))  # Hello, world!
print('------------------------------')

# split
text = 'Hello, world!'
words1 = text
words2 = text
print(words1.split(','))  # ['Hello', ' world!'] => world 앞에 공백도 있음
print(words2.split())  # ['Hello,', 'world!'] 구분자가 없으면 공백 기준
print('------------------------------')

# join
words = ['Hello', 'world!']
new_text = '-'.join(words)
print(new_text)  # Hello-world!
print('------------------------------')

# # capitalize
# text = 'heLLo, woRld!'
# new_text1 = text.capitalize()
# print(new_text1)  # Hello, world!
print('------------------------------')

# # title
# new_text2 = text.title()
# print(new_text2)  # Hello, World!
print('------------------------------')

# # upper
# new_text3 = text.upper()
# print(new_text3)  # HELLO, WORLD!
print('------------------------------')

# # lower
# new_text4 = text.lower()
# print(new_text4)  # hello, world!
print('------------------------------')

# # swapcase
# new_text5 = text.swapcase()
# print(new_text5)  # HEllO, WOrLD!
print('------------------------------')
