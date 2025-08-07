def print_subset(bit):
    for i in range(4):
        if bit[i]:
            print(arr[i], end=" ")
    print(bit)


arr = [7, 5, 8, 1]

bit = [0, 0, 0, 0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l

                print_subset(bit)


print('-------------------------------------------------------------')

arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=", ")
    print(f" : {i:06b}")
print()


print('-------------------------------------------------------------')


N = 10
count_0 = 0

#10개의 정수
numbers = list(map(int, input().split()))

# 원소의 개수가 N개인 집합의 부분집합의 개수는 2**N == 1<<N
# 모든 부분집합을 다 한 번씩 만들어 보고 합이 0이되는지 확인
# 부분집합의 개수만큼 반복(2**N)
for i in range(1<<N):
    # i를 부분집합의 번호(인덱스)라고 생각
    # i를 이진수로 바꿔서 생각
    # 이진수의 각 자릿수는 0 또는 1
    # 이진수의 어떤 자릿수에 1이 있는 경우 -> 그 자리(인덱스)에 있는 원소를 부분집합에 포함
    # 이진수의 어떤 자릿수에 0이 있는 경우 -> 그 자리(인덱스)에 있는 원소는 포함하지 않음

    # 어떤 자리수에 1이 있는지 없는지 어떻게 알아냄?
    # 비트 연산자 & 사용 (True and True === True  // 1 & 1 === 1)
