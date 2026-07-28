T = int(input())
 
for testcase in range(1, T+1):
    N = int(input())
    graph = [[0] * N for _ in range(N)]
 
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
 
    cnt = 1
    x, y, d = 0, 0, 0
 
    for _ in range(N*N):
            graph[x][y] = cnt
            cnt += 1
 
            di = x + dx[d]
            dj = y + dy[d]
             
            if di < 0 or di >= N or dj< 0 or dj >= N or graph[di][dj] != 0 :
               d = (d+1)%4
               di = x + dx[d]
               dj = y + dy[d]
            x, y = di, dj
 
    print(f"#{testcase}")
    for r in graph:
        print(*r)