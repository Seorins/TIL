T = int(input())

for testcase in range(1, T + 1):
    N = int(input())
    box_list = []

    for _ in range(N):
        box_list.append(list(map(int, input().split())))

    # [[2, 2, 4, 4, 1], [3, 3, 6, 6, 2]]

    # 전체 영역 = 10 * 10
    main_box = [[0] * 10 for _ in range(10)]

    # 2 2 4 4 1 [2, 2] -> [4, 4]
    # 3 3 6 6 2 [3, 3] -> [6, 6]

    for i, j, p, q, color in box_list:
        for x in range(i, p + 1):
            for y in range(j, q + 1):
                main_box[x][y] += color

    sum = 0
    for i in range(len(main_box)):
        for j in range(len(main_box)):
            if main_box[i][j] == 3:
                sum += 1

    print(f"#{testcase} {sum}")
