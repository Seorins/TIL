T = int(input())

for testcase in range(1, T + 1):
    N, M = map(int, input().split())
    #   N = 3   M = 5
    main_list = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N):
        for j in range(M):
            s = main_list[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                for c in range(1, main_list[i][j] + 1):
                    ni, nj = i + di * c, j + dj * c
                    if 0 <= ni < N and 0 <= nj < M:
                        s += main_list[ni][nj]

                if max_sum < s:
                    max_sum = s

    print(f"#{testcase} {max_sum}")
