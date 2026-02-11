import heapq

def dijkstra(start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        cur_dist, now = heapq.heappop(pq)

        if dist[now] < cur_dist:
            continue
        
        for nxt_node, weight in graph[now]:
            new_dist = cur_dist + weight
            if new_dist < dist[nxt_node]:
                dist[nxt_node] = new_dist
                heapq.heappush(pq, (new_dist, nxt_node))
    
    return dist


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 다익스트라 3번
dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

# 두 가지 경우
case1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
case2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

answer = min(case1, case2)

# 경로가 없는 경우
if answer == float('inf'):
    print(-1)
else:
    print(int(answer))
