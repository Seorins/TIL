for testcase in range(1, 11):
    N = int(input())
    main_list = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0

    # 가로
    for i in range(100):
        sub_sum = 0
        for j in range(100):
            sub_sum += main_list[i][j]

        if max_sum < sub_sum:
            max_sum = sub_sum

    # 세로
    for j in range(100):
        sub_sum = 0
        for i in range(100):
            sub_sum += main_list[i][j]

        if max_sum < sub_sum:
            max_sum = sub_sum

    # 대각선(왼쪽)
    left_sub_sum = 0
    for i in range(100):
        left_sub_sum += main_list[i][i]

    if max_sum < left_sub_sum:
        max_sum = left_sub_sum

    # 대각선(오른쪽)
    right_sub_sum = 0
    for i in range(100):
        right_sub_sum += main_list[i][100 - 1 - i]

    if max_sum < right_sub_sum:
        max_sum = right_sub_sum

    print(f"#{testcase} {max_sum}")
