# bfs 풀이
from collections import deque

def bfs(x, y) :
    visited = [[False] * 16 for _ in range(16)]
    dq = deque()
    dq.append((x, y))

    visited[x][y] = True

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    while dq: 
        x, y = dq.popleft()

        if graph[x][y] == 3:
            return True
        
        for t in range(4):
            dx = x + di[t]
            dy = y + dj[t]
            if 0 <= dx < 16 and 0 <= dy < 16:
                if graph[dx][dy] != 1 and not visited[dx][dy]:
                    dq.append((dx, dy))
                    visited[dx][dy] = True

    return False

for _ in range(1, 11):
    tc  = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    # 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

    x = y = 1
    
    result = 0
    if bfs(x, y):
        result = 1
    
    print(f"#{tc} {result}")


