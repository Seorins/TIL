'''
1은 집이 있는 곳
0은 집이 없는 곳

연결되었다는 것 -> 좌우 혹은 아래위로 다른 집이 있는 경우

'''
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
    global visited
    
    dq = deque([(x, y)])
    visited[x][y] = True
    
    while dq:
        tx, ty = dq.popleft()
        
        for c in range(4):
            nx, ny = tx + dx[c], ty + dy[c]
             
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    dq.append((nx, ny))
    
    return cnt       
            
    
N = int(input()) # 지도의 크기
board = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        cnt = 0
        if board[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j, 1))

print(len(result))

for r in sorted(result):
    print(r)