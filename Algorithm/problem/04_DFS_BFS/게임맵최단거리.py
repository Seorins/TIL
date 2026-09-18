from collections import deque

def solution(maps):    
    n = len(maps[0])
    m = len(maps)
    
    dist = [[-1] * n for _ in range(m)]
    dq = deque([(0, 0)])
    dist[0][0] = 1
    
    while dq:
        x, y = dq.popleft()
        
        if x == m-1 and y == n-1:
            return dist[x][y]
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
             
            if 0 <= nx < m and 0 <= ny < n:
                if maps[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    dq.append((nx, ny))
                
    return -1
    