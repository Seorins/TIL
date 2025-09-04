import sys
sys.stdin = open('input.txt', 'r')

def dfs(x, y, cnt, dig):
    global max_cnt 
    visited[x][y] = True
    movable = False

    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx, ny = x + di, y + dj
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # i) 그냥 갈 수 있는 경우
            if graph[x][y] > graph[nx][ny]:
                movable = True
                dfs(nx, ny, cnt + 1, dig)
            
            # ii) 파는 거 사용할 경우 
            elif not dig:
                for c in range(1, K+1):
                    if graph[nx][ny]-c < graph[x][y]:
                        graph[nx][ny] -= c
                        movable = True
                        dfs(nx, ny, cnt + 1, 1)
                        graph[nx][ny] += c

    if not movable:
        max_cnt = max(max_cnt, cnt)

    visited[x][y] = False

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_cnt = dig = 0
    cnt = 1

    top = max(map(max, graph))
    # print(top)

    top_lst = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == top:
                top_lst.append((i, j))
    # print(top_lst)
    
    for x, y in top_lst:
        dfs(x, y, cnt, dig)

    print(f"#{tc} {max_cnt}")


