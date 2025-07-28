# 1
text1 = "Hello, Python!"
print(text1.index("o"))  # 4

# 2
# print(text.index("z")) # ValueError: substring not found

# 3
text3 = "HELLO"
print(text3.isupper())  # True

# 4
text4 = "Seorin"

if text4.islower() == True:
    print("소문자입니다")


# 5
text5 = "파이썬"
print(text5.isalpha())

# 6
text6 = "I love Python and learning!"
print(text6.find("l"))  # 2
print(text6.index("l"))  # 2

print(text6.find("z"))  # -1
# print(text6.index("z"))  # ValueError: substring not found


# 7
text7 = input()

if text7.isupper():
    print("통과")
else:
    print("다시 입력하세요")


# 8
text8 = input()

if text8.isalpha():
    print("문자열 확인 완료")
else:
    print("잘못된 입력입니다.")


# -------------------------------------------------------------


# 9
text9 = "I love Python. Python is fun!"
print(text9.replace("Python", "Java", 1))
print(text9.replace("Python", "Java"))

# 10
text10 = "   Hello, World!   "
print(text10.strip())

# 11
text11 = "Learning Python is fun"
sep_text11 = text11.split(" ")
for i in sep_text11:
    print(i)

# 12
text12 = ["2025", "07", "28"]
print("-".join(text12))

# 13
text13 = "heLLo WoRLd"
print(text13.capitalize())  # Hello world 첫 글자만 대문자
print(text13.title())  # Hello World 단어별 첫 글자 대문자
print(text13.swapcase())  # HEllO wOrlD 대소문자 반전


# --------------------------------------------------------------


# 14
text14 = " ***Hello! Python!*** "
split_text14 = text14.split()
print(split_text14)
ls = []

for word in split_text14:
    word2 = word.strip("*! ")
    ls.append(word2)

print("".join(ls))


# 15
text15 = "hello-world-python"
# print(text15.split("-"))
ls = []
for i in text15.split("-"):
    ls.append(i.swapcase())
print(ls)
print("/".join(ls))

# 16
text16 = "I love PyThon and PYTHON is powerful!"
lower_text16 = text16.lower()
print(lower_text16.replace("python", "PYTHON"))

# 17
info = input()
info_ls = info.split("/")
print("이름: ", info_ls[0])
print("나이: ", info_ls[1])
print("도시: ", info_ls[2])

# 18
text18 = "Hello! Python3 is #1 in the world."
text18_ls = text18.split()
lower_ls = []
for word in text18_ls:
    if word.isalpha():
        lower_ls.append(word)

print(lower_ls)

# ------------------------------------------------------------------
