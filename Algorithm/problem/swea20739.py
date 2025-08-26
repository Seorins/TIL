T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    # 가로 
    for i in range(N):
        for j in range(M):
            cnt = 0
            for x, y in [[0, 1]]:
                for k in range(M):
                    dx = i + x 
                    dy = j + y * k
                    if 0 <= dx < N and 0 <= dy < M:
                        if graph[dx][dy] == 1:
                            cnt += 1
            max_cnt = max(cnt, max_cnt)

    # 세로
    for i in range(M):
        for j in range(N):
            cnt = 0
            for x, y in [[1, 0]]:
                for k in range(N):
                    dx = i + x * k
                    dy = j + y 
                    if 0 <= dx < N and 0 <= dy < M:
                        if graph[dx][dy] == 1:
                            cnt += 1
            max_cnt = max(cnt, max_cnt)

    if max_cnt <= 1:
        result = 0 

    else : 
        result = max_cnt

    print(f"#{tc} {result}")
