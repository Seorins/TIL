from collections import deque

N = int(input())
pair = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(pair):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (N+1)

def bfs(s):
    dq = deque([s])
    visited[s] = True
    cnt = -1

    while dq:
        nxt = dq.popleft()
        cnt += 1
        for i in graph[nxt]:
            if not visited[i]:
                dq.append(i)
                visited[i]=True
    return cnt

print(bfs(1))