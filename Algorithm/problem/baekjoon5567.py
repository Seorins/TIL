# 자신의 친구와 친구의 친구

# 학번은 1-N까지 상근이 = 1

from collections import deque

N= int(input()) # 동기의 수
m = int(input()) # 리스트 길이

graph = [[] for _ in range(N+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (N+1)
dq = deque([1])
dist[1] = 0

while dq:
    x = dq.popleft()

    if dist[x] == 2:
        continue

    for nx in graph[x]:
        if dist[nx] == -1:
            dist[nx] = dist[x] + 1
            dq.append(nx)

cnt = 0

for i in range(2, N+1):
    if dist[i] >= 1 and dist[i] <= 2:
        cnt += 1

print(cnt)