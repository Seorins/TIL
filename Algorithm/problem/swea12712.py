T = int(input())

for testcase in range(1, T + 1):
    N, M = map(int, input().split())
    main_list = [list(map(int, input().split())) for _ in range(N)]

    # N = 5, M = 2 (세기)

    # 1 3 3 6 7
    # 8 13 9 12 8
    # 4 16 11 12 6
    # 2 4 1 23 2
    # 9 13 4 7 3

    max_fly = 0
    # + 모양
    for i in range(N):
        for j in range(N):
            s = main_list[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                for c in range(1, M):
                    ni, nj = i + di * c, j + dj * c
                    if 0 <= ni < N and 0 <= nj < N:
                        s += main_list[ni][nj]

            if max_fly < s:
                max_fly = s

    # X 모양
    for i in range(N):
        for j in range(N):
            s = main_list[i][j]
            for di, dj in [[-1, 1], [1, 1], [1, -1], [-1, -1]]:
                for c in range(1, M):
                    ni, nj = i + di * c, j + dj * c
                    if 0 <= ni < N and 0 <= nj < N:
                        s += main_list[ni][nj]
            if max_fly < s:
                max_fly = s

    print(f"#{testcase} {max_fly}")
