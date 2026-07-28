from heapq import heappop, heappush

def dijkstra(sx, sy):
    pq  = [(0, sx, sy)]
    oils = [[float('inf')]* N for _ in range(N)]
    oils[sx][sy] = 0
    while pq:
        oil, x, y = heappop(pq)

        if oils[x][y] < oil : 
            continue

        for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            nx, ny = x + di, y + dj
            if 0 <= nx < N and 0 <= ny < N:
                # 높을 때로 해줘야 함 !!! abs쓰면 낮아도 무조건임
                new_oil = oil + 1 + max(0, graph[nx][ny] - graph[x][y])

                if oils[nx][ny] <= new_oil:
                    continue

                oils[nx][ny] = new_oil
                heappush(pq, (new_oil, nx, ny))

    return oils

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 0, 0에서 시작 하고 마지막은 N-1, N-1이 마지막임
    # 움직이면서 누적 연료를 가지고 움직여야 함
    # 기본적으로 1씩 들고 더 높은 곳으로 가면 차이만큼 추가 
    
    result = dijkstra(0, 0)

    print(f"#{tc} {result[N-1][N-1]}")