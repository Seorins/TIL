def change(x, y):
    max_num = -float('inf')
    mx, my = -1, -1

    for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        nx , ny = x + di, y + dj
        if 0 <= nx < N and 0 <= ny < N :
            if max_num < grid[nx][ny]:
                

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


for c in range(1, N**2 + 1):
    next = False
    for i in range(N):
        for j in range(N):
            if grid[i][j] == c:
                change(i, j)
                next = True
            if next : 
                break
        if next : 
            break

