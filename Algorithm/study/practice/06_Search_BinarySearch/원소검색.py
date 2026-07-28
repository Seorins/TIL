N = 5
A = [1, 2, 3, 4, 5]

# 찾고자 하는 값
key = 4

# 반복문을 통해 key 가 있는지 검사
for i in range(N):
    if A[i] == key:
        print("찾았다", i)
        break
else:
    print("없음")

# 재귀함수를 통해서 key 가 있는지 검사
def search():
    # 종료

    # 재귀호출
