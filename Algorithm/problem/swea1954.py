T = int(input())

for testcase in range(1, T + 1):
    N = int(input())

    main_list = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i = j = 0  # [0, 0]
    dir = 0  # 방향
    num = 1

    while num <= N * N:
        main_list[i][j] = num
        num += 1

        dx = i + di[dir]
        dy = j + dj[dir]

        if dx < 0 or dx >= N or dy < 0 or dy >= N or main_list[dx][dy] != 0:
            # dir 0 -> 1 -> 2 -> 3 -> 0
            if dir == 3:
                dir = 0
            else:
                dir += 1

            dx = i + di[dir]
            dy = j + dj[dir]

        i, j = dx, dy

    print(f"#{testcase}")
    for row in main_list:
        print(*row)
