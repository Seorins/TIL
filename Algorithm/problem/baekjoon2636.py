from collections import deque

# 1. bfs통해서 바깥 0 표시해주기 
def bfs():
    dq = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while dq:
        x, y = dq.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + di, y + dj
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
    
    return visited

# 2. 치즈 중에서 외부공기랑 접촉 되어 있으면 녹여주면 됨
def melt():
    global time, cnt_lst, board
    visited = bfs()
    cnt = 0

    n_board = [r[:] for r in board]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nx , ny = i + di, j + dj
                    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
                        n_board[i][j] = 0
                        cnt += 1
                        break

    board = n_board
    time += 1
    cnt_lst.append(cnt)
    return cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cnt_lst = []
time = 0

# 다 녹일 때까지 돌림
while True:
    finish = melt()
    if finish == 0:
        break

print(time-1)
print(cnt_lst[-2] if len(cnt_lst) >= 2 else 0)