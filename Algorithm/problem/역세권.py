import heapq

def dijkstra(trains):
    dists = [float('INF')] * (N+1)
    heap = []

    # 모든 기차역이 있는 도시를 시작점으로 설정
    for train in trains : 
        dists[train] = 0
        heapq.heappush(heap, (0, train))

    while heap: 
        dist, node = heapq.heappop(heap)

        if dists[node] < dist : 
            continue

        for nxt_node, nxt_cost in graph[node]:
            new_dist = dist + nxt_cost
            if dists[nxt_node] <= new_dist:
                continue
            dists[nxt_node] = new_dist
            heapq.heappush(heap, (new_dist, nxt_node))

    return dists

N, M, K, L = map(int , input().split()) # 도시 수, 도로 수?, 기차 역 수, 최소 거리(역세권 조건 L보다 이하여야 함)
trains = list(map(int, input().split())) # 기차역이 있는 도시 
graph = [[] for _ in range (N+1)]

for _ in range (M):
    start, end, weight = map(int, input().split()) 
    graph[start].append((end, weight)) 
    # graph[end].append((start, weight)) # 양방향인지 단방향인지 문제가 기억이 안남

dists = dijkstra(trains)

cnt = 0
for dist in dists: 
    if dist <= L : 
        cnt += 1

print(cnt)