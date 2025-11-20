# N개의 도시 중 K개의 도시에 면접장 배치 / 단방향
# 면접장까지의 거리가 가장 먼 도시와 그 거리 
from heapq import heappop, heappush

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    start, end, weignt = map(int, input().split())
    graph[end].append((weignt, start))

cities = list(map(int, input().split()))

pq = []
dists = [float('inf')] * (N+1)

for c in cities:
    dists[c] = 0
    heappush(pq, (0, c))

while pq:
    dist, node = heappop(pq)

    if dists[node] < dist:
        continue

    for nxt_dist, nxt_node in graph[node]:
        new_dist = dist + nxt_dist

        if dists[nxt_node] > new_dist:
            dists[nxt_node] = new_dist
            heappush(pq, (new_dist, nxt_node))

max_city = 1
max_dist = dists[1]

for i in range(2, N+1):
    if dists[i] > max_dist:
        max_dist = dists[i]
        max_city = i

print(max_city)
print(max_dist)