import sys
sys.stdin = open("input.txt", "r")

'''
연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
최대가 되는 수식과 최소가 되는 수식을 찾고 두 값의 차이를 구하기

+ = x /

숫자는 순서대로 유지
연산자만 순서 바뀌면서 하기 
'''

def dfs(idx, num, plus, minus, mul, div):
    global max_num
    global min_num

    if idx == N: 
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return 
    
    nxt_num = number[idx]

    if plus > 0 :
        dfs(idx+1, num + nxt_num, plus-1, minus, mul, div)

    if minus > 0 :
        dfs(idx+1, num - nxt_num, plus, minus-1, mul, div)

    if mul > 0 :
        dfs(idx+1, num * nxt_num, plus, minus, mul-1, div)

    if div > 0 :
        dfs(idx+1, int(num / nxt_num), plus, minus, mul, div-1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    plus, minus, mul, div = list(map(int, input().split())) 
    number = list(map(int, input().split()))
    max_num = -float('inf')
    min_num = float('inf')
    num = number[0]

    dfs(1, num, plus, minus, mul, div)

    print(f"#{tc} {max_num - min_num}")