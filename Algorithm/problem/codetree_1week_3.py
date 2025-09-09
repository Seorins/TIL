n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = i + di, j + dj 
            if 0 <= nx < n and 0 <= ny < n :
                if grid[nx][ny] == 1:
                    cnt += 1
        if cnt >= 3:
            total += 1
                
print(total)
