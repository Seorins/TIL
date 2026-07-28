def road(cnt):
    if cnt == N-1: 
        path_lst.append([1]+path+[1])
        return
    
    for num in range(2, N+1):
        if used[num]:
            continue

        used[num] = True
        path.append(num)
        road(cnt+1)
        path.pop()
        used[num] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * (N + 1)
    path = []
    path_lst = []
    road(0)

    min_total = float('inf')
    for pth in path_lst:
        total = 0
        for i in range(len(pth)-1):
            total += graph[pth[i]-1][pth[i+1]-1]
        min_total = min(min_total, total)

    print(f"#{tc} {min_total}")

