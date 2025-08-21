from collections import deque

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _  in range(N)]

def bfs(s_x, s_y, visited):
    dq = deque()
    dq.append((s_x, s_y))
    visited[s_x][s_y] = True
    num = 0

    while dq:
        x, y = dq.popleft()

        num += graph[x][y]

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            dx, dy = x + di, y + dj
            if 0 <= dx < N and 0 <= dy < N :
                if not visited[dx][dy] and graph[dx][dy] == 1:
                    dq.append((dx, dy))
                    visited[dx][dy] = True
    return num

result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j, visited))

result.sort()
print(len(result))
for r in result:
    print(r)