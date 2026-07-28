T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    max_cnt = 0
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            x, y = i, j
            cnt = 1
            
            while True : 
                moved = False
                nx, ny = -1, -1
                min_num = float('inf')

                for t in range(4):
                    dx = x + di[t]
                    dy = y + dj[t]

                    if 0 <= dx < N and 0 <= dy < N:
                        if graph[dx][dy] < graph[x][y] :
                           if graph[dx][dy] < min_num : 
                                min_num = graph[dx][dy]
                                nx, ny = dx, dy
                                moved = True

                if moved:
                    x, y = nx, ny 
                    cnt += 1

                else :
                    break
        
            max_cnt = max(cnt, max_cnt)

    print(f"#{tc} {max_cnt}")