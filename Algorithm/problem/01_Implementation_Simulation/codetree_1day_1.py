n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

x, y = 0, 0

dir_dict = {'N':(1, 0), 'E':(0, 1), 'S':(-1, 0), 'W':(0, -1)}

for i in range(n):
    di, dj = dir_dict[dir[i]]
    nx = x + di * dist[i]
    ny = y + dj * dist[i]
    x, y = nx, ny

print(y, x)


