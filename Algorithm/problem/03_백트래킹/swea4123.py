# 우선 순위 고려 x / 왼쪽 -> 오른쪽
# 최대, 최소 구하고 두 값의 차

# 계산 함수
# 각 연산자 넣고 값 계산하기 
def calculate(plus, minus, multi, divide, idx, num):
    global max_num, min_num, visited

    # 가지치기 
    key = (idx, plus, minus, multi, divide, num)
    if key in visited:
        return
    visited.add(key)


    # 종료 조건
    if idx == N :
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return 
    
    x = numbers[idx]

    if plus > 0 :
        calculate(plus-1, minus, multi, divide, idx+1, num+x)

    if minus > 0 :
        calculate(plus, minus-1, multi, divide, idx+1, num-x)

    if multi > 0 :
        calculate(plus, minus, multi-1, divide, idx+1, num*x)

    if divide > 0:
            calculate(plus, minus, multi, divide-1, idx+1, int(num/x))
        
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    plus, minus, multi, divide = map(int, input().split())
    numbers = list(map(int, input().split()))
    visited = set()

    max_num = -float('inf')
    min_num = float('inf')
    
    calculate(plus, minus, multi, divide, 1, numbers[0])
    print(f"#{tc} {max_num - min_num}")