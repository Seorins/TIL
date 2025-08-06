T = int(input())

for testcase in range(1, T + 1):
    N, M = map(int, input().split())

    main_box = [[0] * N for _ in range(N)]
    # sub_box = [[0] * N for _ in range(M)]

    # N = 3 , M = 2
    cnt = 1
    for i in range(N - M + 1):  # 0, 1
        for j in range(N - M + 1):  # 0, 1
            for p in range(M):  # 0, 1
                for q in range(M):  # 0, 1
                    main_box[i + p][j + q] = cnt
            cnt += 1

    print(f"#{testcase}")
    for i in range(N):
        for j in range(N):
            print(main_box[i][j], end=" ")
        print()
