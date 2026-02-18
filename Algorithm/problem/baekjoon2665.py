import sys
from collections import deque

input = sys.stdin.readline

# 동, 서, 남, 북
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

n = int(input())
grid = [list(input().strip()) for _ in range(n)]

dist = [[float('inf')] * n for _ in range(n)] 
dist[0][0] = 0

dq = deque()
dq.append((0, 0))

while dq:
    x, y = dq.popleft()

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if not (0 <= nx < n and 0 <= ny < n):
            continue

        # 흰 방 = 0, 검은 방 = 1
        cost = 0 if grid[nx][ny] == '1' else 1
        nd = dist[x][y] + cost

        if nd < dist[nx][ny]:
            dist[nx][ny] = nd

            if cost == 0:
                dq.appendleft((nx, ny))
            else:
                dq.append((nx, ny))

print(dist[n - 1][n - 1])
