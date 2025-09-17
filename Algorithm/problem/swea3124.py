from heapq import heappop, heappush

def prim(start):
    pq = [(0, start)]
    MST = [0] * (V+1)
    min_weight = 0

    while pq:
        weight, node = heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for n_weight, n_node in graph[node]:
            if not MST[n_node]:
                heappush(pq, (n_weight, n_node))

    return min_weight

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)] 

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
        graph[e].append((w, s)) 

    print(f"#{tc} {prim(0)}")