n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

row = []
for i in range(n): # 행
    movable = True
    for j in range(k-1, k+m-1): #열
        if grid[i][j] != 0:
            movable = False
            break
    if not movable:
        break
    
    else:
        row.append(i)

for j in range(k-1, k+m-1):
    grid[row[-1]][j] = 1

for r in grid:
    print(*r)