T = int(input())

for testcase in range(1, T + 1):
    N, K = map(int, input().split())
    main_list = [list(map(int, input().split())) for _ in range(N)]

    # N = 5  K = 3

    cnt = 0
    # 열순회
    for j in range(N):  # 0, 1, 2, 3, 4
        for i in range(N - K + 1):  # 0, 1, 2
            sub_cnt = 0
            for p in range(K):  # 0, 1, 2
                if main_list[i + p][j] == 1:
                    sub_cnt += 1
            if sub_cnt == K:
                before = (i == 0) or (main_list[i - 1][j] == 0)
                after = (i + K >= N) or (main_list[i + K][j] == 0)
                if before and after:
                    cnt += 1

    # 행순회
    for i in range(N):  # 0, 1, 2, 3, 4
        for j in range(N - K + 1):  # 0, 1, 2
            sub_cnt = 0
            for p in range(K):  # 0, 1, 2
                if main_list[i][j + p] == 1:
                    sub_cnt += 1
            if sub_cnt == K:
                before = (j == 0) or (main_list[i][j - 1] == 0)
                after = (j + K >= N) or (main_list[i][j + K] == 0)
                if before and after:
                    cnt += 1

    print(f"#{testcase} {cnt}")
