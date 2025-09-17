# n = 격자 크기 / r, c = 시작 위치
n, r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [graph[r-1][c-1]]
x, y = r-1, c-1

while True:
    movable = False

    max_num = graph[x][y]
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + di, y + dj
        if 0 <= nx < n and 0 <= ny < n : 
            if graph[nx][ny] > max_num : 
                max_num = graph[nx][ny]
                movable = True
                break

    if movable:
        result.append(graph[nx][ny])
        x, y = nx, ny

    else:
        break

print(result)
