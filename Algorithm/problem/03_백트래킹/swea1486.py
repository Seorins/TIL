def dfs(idx, total):

    if total >= min_h:
        return 

    if total >= B:
        min_h = min(total, min_h)
        return 

    if idx == N :
        return 
    
    dfs(idx+1, total+height[idx])
    dfs(idx+1, total)

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    # min_h = float('inf') # 나올 수 있는 최대 범위 (정답이 보장된 경우)
    min_h = 10000 * N # 나올 수 없다면 최대 값으로 지정

    dfs(0, 0)

    print(f"{tc} {min_h - B}")