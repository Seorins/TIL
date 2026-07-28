from collections import deque

def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    visited[i][j] = True

    while dq:
        x, y = dq.popleft()
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            dx, dy = x + di, y + dj
            if 0 <= dx < N and 0 <= dy < M :
                if not visited[dx][dy] and graph[dx][dy] == 1:
                    visited[dx][dy] = True
                    dq.append((dx, dy))


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*(M) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            cnt += 1

print(cnt)