# N개의 물건 최대 C만큼 넣을 수 있는 가방
# N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램

n, c = map(int, input().split())

things = list(map(int, input().split()))

# 모든 경우 보면 터짐 

mid = n // 2
left = things[:mid]
right = things[mid:]

# 투포인터 활용

def sums(arr, idx, now, result):
    if now > c: 
        return 
    if idx == len(arr):
        result.append(now)
        return 
    
    # 선택 x
    sums(arr, idx+1, now, result)
    
    # 선택 o
    sums(arr, idx+1, now + arr[idx], result)

left_sum = []
right_sum = []

sums(left, 0, 0, left_sum)
sums(right, 0, 0, right_sum)

left_sum.sort()
right_sum.sort()

i = 0
j = len(right_sum) - 1
ans = 0

while i < len(left_sum) and j >= 0:
    if left_sum[i] + right_sum[j] <= c:
        ans += (j+1)
        i += 1

    else: 
        j -= 1

print(ans)

