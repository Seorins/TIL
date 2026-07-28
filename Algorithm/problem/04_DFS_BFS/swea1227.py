from collections import deque

def bfs(s_x, s_y):
    visited = [[False]*100 for _ in range(100)]
    dq =deque()
    dq.append((s_x, s_y))
    visited[s_x][s_y] = True

    while dq:
        x, y = dq.popleft()
        
        if graph[x][y] == 3:
            return 1
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            dx, dy = di + x, dj + y
            if 0 <= dx < 100 and 0 <= dy < 100:
                if graph[dx][dy] != 1 and not visited[dx][dy]:
                    visited[dx][dy] = True
                    dq.append((dx, dy))
    return 0

for _ in range(10):
    tc = int(input())
    graph = [list(map(int, input())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if graph[i][j] == 2:
                s_x, s_y = i, j

    print(f"#{tc} {bfs(s_x, s_y)}")