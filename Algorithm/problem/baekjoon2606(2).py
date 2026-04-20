'''
컴퓨터가 연결되어 있고 하나가 감염되었을 때 
그 하나로 인해서 감염되는 컴퓨터 개수 
'''
from collections import deque

def bfs(x):
    global cnt
    
    visited = [False] * (N+1)
    dq = deque([x])
    visited[x] = True

    while dq:
        x = dq.popleft()

        for nx in graph[x]:
            if not visited[nx]:
                cnt += 1
                visited[nx] = True
                dq.append(nx)
                
    return cnt
    
N = int(input()) # 컴퓨터의 수 
pair = int(input()) # 연결된 컴퓨터의 수 
graph = [[] for _ in range(N+1)]
cnt = 0

for _ in range(pair):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x) # 양방향 할 지 확인 

print(bfs(1))