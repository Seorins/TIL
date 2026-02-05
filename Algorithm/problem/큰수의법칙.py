# 다양한 수로 이루어진 배열이 있을 때 M번 더하여 가장 큰 수 만들기
# K = 동일한 인덱스 연속해서 더할 수 있는 개수 (수가 같아도 인덱스만 다르면 됨)

'''
N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort() # 작은 수부터 정렬

result = 0

while True:

    for i in range(K):
        if M == 0:
            break
        result += numbers[N-1]
        M -= 1

    if M == 0:
        break

    result += numbers[N-2]
    M -= 1
    
print(result)
'''

N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[N-1]
second = data[N-2]

cnt = int(M / (K+1)) * K
cnt += M % (K+1)

result = 0
result += (cnt) * first
result += (M-cnt) * second

print(result)