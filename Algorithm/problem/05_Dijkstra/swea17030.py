from heapq import heappop, heappush

def dijkstra(start):
    pq = [(0, start)]
    dists = [float('inf')] * E # 여기다가 최단 거리 기록해둘거임!
    dists[start] = 0

    while pq:
        dist, node = heappop(pq)

        # 이미 들어 있는 게 있는데 그게 더 작으면 넘어갈 거임
        if dists[node] < dist :
            continue

        for next_dist, next_node in graph[node]:

            # 다음 곳으로 가기 위한 누적 거리
            new_dist = dist + next_dist

            if dists[next_node] <= new_dist : 
                continue

            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))


    return dists


T = int(input())

for tc in range(1, T+1):
    # N이 마지막 연결지점 번호 
    # E가 도로의 개수 
    N, E = map(int, input().split())
    graph = [[] for _ in range(E)]
    start = 0

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e)) 


    result = dijkstra(0)

    print(f"#{tc} {result[N]}")