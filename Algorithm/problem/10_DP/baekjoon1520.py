'''
1. 메모리 터짐 이슈 [dfs + dp]

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 하, 우, 상, 좌)
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = [[-1] * m for _ in range(n)]


def dfs(x, y):

    # 도착점 도달 → 경로 1개 완성
    if x == n - 1 and y == m - 1:
        return 1

    # 이미 방문한 곳일 때 
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if graph[x][y] > graph[nx][ny]:
                visited[x][y] += dfs(nx, ny)

    return visited[x][y]

print(dfs(0, 0))

'''

# 2. 반복 dp

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = 1  # 시작점에서 출발하는 경로 수 1로 시작

cells = []
for i in range(n):
    for j in range(m):
        cells.append((board[i][j], i, j))

# 높이 내림차순(높은 곳 -> 낮은 곳)으로 순회
cells.sort(reverse=True)

moves = [(1,0), (-1,0), (0,1), (0,-1)]

for h, x, y in cells:
    if dp[x][y] == 0:
        continue

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] < h:
            dp[nx][ny] += dp[x][y]

print(dp[n-1][m-1])
