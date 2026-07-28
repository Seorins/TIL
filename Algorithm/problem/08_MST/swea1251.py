from heapq import heappush, heappop

def prim(start):
    pq = [(0, start)]
    MST = [0] * N
    min_weight = 0

    while pq:
        weight, node = heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for next_weight, next_node in graph[node]:
            if not MST[next_node]:
                heappush(pq, (next_weight, next_node))

    return min_weight

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[] for _ in range(N)]
    x_arr = list(map(int, input().split()))
    y_arr = list(map(int, input().split()))
    E = float(input())
    graph = [[] for _ in range(N)]


    for i in range(N):
        arr[i].append((x_arr[i], y_arr[i]))

# 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L^2)만큼 지불
# 해저 길이 = abs(x1 - x2) + abs(y1 - y2)

    for i in range(N):
        for j in range(N):
            graph[i].append(((E * (abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])^2)), j))
            graph[j].append(((E * (abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])^2)), i))

    result = prim(0)

    print(f"#{tc} {result}")




