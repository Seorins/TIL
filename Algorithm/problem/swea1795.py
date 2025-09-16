import sys
sys.stdin = open("input.txt", "r")

from heapq import heappop, heappush

def dijkstra(start, graph):
    pq = [(0, start)]
    dists = [float('inf')] * (N+1)
    dists[start] = 0

    while pq : 
        dist, node = heappop(pq)

        if dists[node] < dist : 
            continue

        for n_dist, n_node in graph[node]:
            
            new_dist = dist + n_dist
            
            if dists[n_node] <= new_dist:
                continue

            dists[n_node] = new_dist
            heappush(pq, (new_dist, n_node))

    return dists

T = int(input())

for tc in range(1, T+1):
    # 도로는 단 방향이라서 오고 갈 때가 다름
    # N = 집 개수 M = 입력 받을 줄 개수  X = 인수네 집
    # 각 노드들의 최단 시간 중에서 가장 오래 걸리는 시간을 선택해야 함
    N, M, X = map(int, input().split())
    soo_graph = [[] for _ in range(N+1)]
    home_graph = [[] for _ in range(N+1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        soo_graph[x].append((c, y)) 
        home_graph[y].append((c, x))

    soo_result = dijkstra(X, soo_graph)
    home_result = dijkstra(X, home_graph)

    max_result = 0
    for i in range(1, N+1):
        max_result = max(soo_result[i] + home_result[i], max_result)

    print(f"#{tc} {max_result}")