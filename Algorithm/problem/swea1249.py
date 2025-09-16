import sys
sys.stdin = open('input.txt', 'r')

'''
S부터 G까지 가기 위한 도로 복구 작업 빠르게 수행
깊이에 따라서 비례해서 시간 증가
복구 시간이 가장 짧은 경로에 대한 총 복구 시간 (누적 시간 => 다익스트라)

좌상단 S 우하단 G 상하좌우 한 칸씩 
현재 칸을 복구해야만 다른 곳으로 이동 가능!
'''

from heapq import heappop, heappush

def dijkstra(sx, sy):
    pq = [(0, sx, sy)]
    times = [[float('inf')]*N for _ in range(N)]
    times[sx][sy] = graph[sx][sy]

    while pq:
        time, x, y = heappop(pq)

        if times[x][y] < time:
            continue

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = x + di, y + dj
            if 0 <= nx < N and 0 <= ny < N :
                new_time = time + graph[nx][ny]

                if times[nx][ny] <= new_time:
                    continue

                times[nx][ny] = new_time
                heappush(pq, (new_time, nx, ny))

    return times

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    result = dijkstra(0, 0)
    
    print(f"#{tc} {result[N-1][N-1]}")