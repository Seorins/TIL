from collections import deque

def bfs(i, j , visited, land):
    dq = deque([(i, j)])
    visited[i][j] = True
    cnt = 1
    visited_col = {j}
    
    while dq:
        x, y = dq.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + di, y + dj
            if 0 <= nx < len(land) and 0 <= ny < len(land[0]):
                if land[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    visited_col.add(ny)            
                    cnt += 1
                    dq.append((nx, ny))
    
    return cnt, visited_col

def solution(land):
    visited = [[False]*(len(land[0])) for _ in range(len(land))]
    col_cnt = [0] * len(land[0])
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and not visited[i][j]:
                cnt, visited_col = bfs(i, j, visited, land)
                
                for col in visited_col:
                    col_cnt[col] += cnt
    
    return max(col_cnt)