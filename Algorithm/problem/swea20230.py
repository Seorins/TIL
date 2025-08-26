T = int(input())

for testcase in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 같은 행과 열 모두 터트리기 

    max_score = 0 

    for i in range(N):
        for j in range(N):
            score = graph[i][j]
            #[2, 2] 2행 2열 모두 팡
            for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                for c in range(1, N):
                    di = i + dx * c
                    dj = j + dy * c

                    if 0 <= di < N and 0 <= dj < N:
                        score += graph[di][dj]
                    else:
                        break

            if max_score < score:
                max_score = score

    print(f"#{testcase} {max_score}") 
            
            
