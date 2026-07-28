from collections import deque

T = int(input())

def bfs(x, y):
    visited = [[False]*N for _ in range(N)]
    dist = [[0]*N for _ in range(N)]
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True

    while dq:
        x, y = dq.popleft()

        if graph[x][y] == 3:
            return dist[x][y]-1
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            dx = di + x
            dy = dj + y
            if 0 <= dx < N and 0 <= dy < N and graph[dx][dy] != 1 and not visited[dx][dy]:
                dist[dx][dy] = dist[x][y] + 1
                visited[dx][dy] = True
                dq.append((dx, dy))
    return 0

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    x = y = -1

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                x, y = i, j

    print(f"#{tc} {bfs(x, y)}")