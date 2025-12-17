T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    max_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for p in range(M):
                for q in range(M):
                    fly += graph[i+p][j+q]

            max_fly = max(max_fly, fly)

    print(f"#{tc} {max_fly}")