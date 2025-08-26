T = int(input())

for testcase in range(1, T + 1):
    main_list = [list(map(int, input().split())) for _ in range(9)]

    cnt = 0
    result = 0

    # 가로
    # 45
    for i in range(9):
        sub_sum = 0
        for j in range(9):
            sub_sum += main_list[i][j]
        if sub_sum == 45:
            cnt += 1

    # 세로
    for j in range(9):
        sub_sum = 0
        for i in range(9):
            sub_sum += main_list[i][j]
        if sub_sum == 45:
            cnt += 1

    # 칸
    for i in range(0, 9, 3):  # 0, 3, 6
        for j in range(0, 9, 3):  # 0, 3, 6
            sub_sum = 0
            for p in range(3):  # 0, 1, 2
                for q in range(3):
                    sub_sum += main_list[i + p][j + q]

            if sub_sum == 45:
                cnt += 1

    if cnt == 27:
        result = 1

    print(f"#{testcase} {result}")
