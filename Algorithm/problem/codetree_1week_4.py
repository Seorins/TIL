n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dir_dict = {'U':(-1, 0), 'D':(1, 0), 'R':(0, 1), 'L':(0, -1)}

for _ in range(t):
    di, dj = dir_dict[d]
    nx, ny = r + di, c + dj

    if nx < 1 or nx > n or ny < 1 or ny > n:
        if d == 'U': d = 'D'
        elif d == 'D': d = 'U'
        elif d == 'R': d = 'L'
        elif d == 'L': d = 'R'
        continue

    r, c = nx, ny

print(r, c)