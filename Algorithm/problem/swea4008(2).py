# 연산자 +, -, x, /
# 우선순위 고려 x, 왼쪽에서 오른쪽 차례대로 계산
# 최대와 최소의 차이

def dfs(idx, num, plus, minus, mul, div):
    global max_num
    global min_num

    # 종료 조건
    if idx == N:
        max_num = max(num, max_num)
        min_num = min(num, min_num)
        return 

    nxt = numbers[idx]

    # 수식 하나씩 줄여가면서 백트래킹
    if plus > 0:
        dfs(idx+1, num+nxt, plus-1, minus, mul, div)

    if minus > 0:
        dfs(idx+1, num-nxt, plus, minus-1, mul, div)

    if mul > 0:
        dfs(idx+1, num*nxt, plus, minus, mul-1, div)

    if div > 0:
        dfs(idx+1, int(num/nxt), plus, minus, mul, div-1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    plus, minus, mul, div = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_num = -100000000 
    min_num = 100000000

    dfs(1, numbers[0], plus, minus, mul, div)

    print(f"#{tc} {max_num-min_num}")