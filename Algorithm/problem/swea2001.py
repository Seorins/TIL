T = int(input())

for testcase in range(1, T + 1):
    N, M = map(int, input().split())

    main_list = [list(map(int, input().split())) for _ in range(N)]

    # 1 3 3 6 7
    # 8 13 9 12 8
    # 4 16 11 12 6
    # 2 4 1 23 2
    # 9 13 4 7 3

    max_sum = 0
    # N = 5, M = 2
    for i in range(N - M + 1):  # 0 - 4 [1, 0] [2, 0]
        for j in range(N - M + 1):  # 0 - 4
            sum = 0
            for p in range(M):  # 0 - 1
                for q in range(M):  # 0 -1
                    sum += main_list[p + i][q + j]
            if max_sum < sum:
                max_sum = sum

    print(f"#{testcase} {max_sum}")
