from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            # 익은 토마토(1)의 좌표를 큐에 저장
            q.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    for i in range(4):
        # 익은 토마토 상하좌우 돌면서 일수 저장
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append([nx, ny])

result = 0
for line in board:
    for tomato in line:
        if tomato == 0:
            # 안익은 토마토(0)이 있으면 바로 정지
            print(-1)
            exit()
    result = max(result, max(line))
    
# 1에서 시작했기 때문에 결과 값에서 1빼주기
print(result-1)