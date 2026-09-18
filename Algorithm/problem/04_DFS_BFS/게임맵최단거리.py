from collections import deque

def solution(maps):    
    min_cnt = 10001
    n = len(maps[0])
    m = len(maps)
    visited = [[False] * n for _ in range(m)]
    dq = deque([(0, 0)])
    visited[0][0] = True
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    cnt = 0
    while dq:
        x, y = dq.popleft()
        cnt += 1
        
        if x == n-1 and y == m-1:
            min_cnt = min(min_cnt, cnt)
        
        for c in range(4):
            dx = x + di[c]
            dy = y + dj[c]
             
            if maps[dx][dy] == 1 and not visited[dx][dy]:
                visited[dx][dy] = True
                dq.append((dx, dy))
                
    return -1 if min_cnt == 10001 else min_cnt
    