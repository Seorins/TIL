from collections import deque

def bfs(i, j, visited):
    dq = deque()
    dq.append((i, j))
    visited[i][j] = True

    while dq:
        x, y = dq.popleft()

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            dx, dy = x + di, y + dj 
            if 0 <= dx < N and 0 <= dy < M :
                if not visited[dx][dy] and graph[dx][dy] == 1:
                    dq.append((dx, dy))
                    visited[dx][dy] = True
    return visited

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    cnt = 0

    for i in range(K):
        p, q = map(int, input().split())
        graph[q][p] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                if bfs(i, j, visited):
                    cnt += 1

    print(cnt)