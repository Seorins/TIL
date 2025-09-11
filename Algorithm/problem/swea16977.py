def dfs(idx, cnt):
    global min_cnt

    if cnt >= min_cnt:
        return 

    # 종료 조건
    if idx >= N-1 :
        min_cnt = min(min_cnt, cnt)
        return 
    
    for i in range(1, station[idx] + 1):
        n_idx = idx + i
        
        dfs(n_idx, cnt + 1)

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    station = arr[1:]
    min_cnt = float('inf')
    
    dfs(0, 0)
     
    print(f"#{tc} {min_cnt-1}")