def recur(x, y, cnt, total):
    global min_len
    ex, ey = home

    if total >= min_len : 
        return 
    
    if cnt == N : 
        total += (abs(ex-x) + abs(ey-y))
        min_len = min(min_len, total)
        return 

    for j in range(N):
        if used[j] == False:
            used[j] = True
            nx, ny = customer[j] 
            recur(nx, ny, cnt+1, total+(abs(nx-x) + abs(ny-y)))
            used[j] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    graph = [[0] * 100 for _ in range(100)]
    min_len = float('inf')
    used = [False] * N 

    company = arr[0:2]
    home = arr[2:4]
    customer = [[arr[i], arr[i+1]] for i in range(4, len(arr), 2)]

    x, y = company
    recur(x, y, 0, 0)
    # (x1, y1)와 (x2, y2) 사이의 거리는 |x1-x2| + |y1-y2|
    # 경로 중 가장 짧은 것을 찾으면 됨 

    print(f"#{tc} {min_len}")
