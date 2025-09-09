dirs = input()

# 좌표평면 @!!!!!1

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
x = y = dir = 0

for d in dirs:
    if d == 'L':
        dir = (dir+3) % 4

    if d == 'R':
        dir = (dir+1) % 4

    if d == 'F':
        di, dj = direction[dir]
        nx = x + di
        ny = y + dj
        x, y = nx, ny
    
print(y, x)

