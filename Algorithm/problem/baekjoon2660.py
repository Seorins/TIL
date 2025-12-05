from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dist = [-1] * (n+1)
    q = deque([start])
    dist[start] = 0

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)

    return max(dist[1:])  

scores = []

min_score = float('inf')
for i in range(1, n+1):
    s = bfs(i)
    scores.append(s)
    min_score = min(min_score, s)


candidates = []
for i in range(1, n+1):
    if scores[i-1] == min_score:
        candidates.append(i)

print(min_score, len(candidates))
print(*candidates)
