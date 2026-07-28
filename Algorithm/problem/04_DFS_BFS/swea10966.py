from collections import deque

def bfs():
    # visited = [[False] * M for _ in range(N)]
    dist = [[-1] * M for _ in range(N)]
    dq = deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'W':
                dq.append((i, j))
                # visited[i][j] = True
                dist[i][j] = 0

    while dq : 
        x, y = dq.popleft()

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            dx = x + di
            dy = y + dj
            if 0 <= dx < N and 0 <= dy < M :
                if dist[dx][dy] == -1 :
                # if not visited[dx][dy] :
                    dq.append((dx, dy))
                    # visited[dx][dy] = True
                    dist[dx][dy] = dist[x][y] + 1
    return dist

T = int(input().strip())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(input()) for _ in range(N)]

    dist = bfs()

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'L':
                cnt += dist[i][j]
    
    print(f"#{tc} {cnt}")


