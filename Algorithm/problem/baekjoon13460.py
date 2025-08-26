def dfs(bx, by, rx, ry):
    dist = [[-1] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                pass

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

bx = by = rx = ry = -1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'B':
            bx, by = i, j
        if graph[i][j] == 'R':
            rx, ry = i, j

dfs(bx, by, rx, ry)
        