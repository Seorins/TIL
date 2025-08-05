T = int(input())
result = []

for i in range(T):
    nums = int(input())

    counts = [0] * 12

    for j in range(6):
        counts[nums % 10] += 1
        nums //= 10

    run_cnt = trp_cnt = 0

    j = 0
    while j < 10:
        if counts[j] >= 3:
            counts[j] -= 3
            trp_cnt += 1
            continue
        if counts[j] >= 1 and counts[j + 1] >= 1 and counts[j + 2] >= 1:
            counts[j] -= 1
            counts[j + 1] -= 1
            counts[j + 2] -= 1
            run_cnt += 1
            continue
        j += 1

    if run_cnt + trp_cnt == 2:
        print(f"#{i+1} Baby Gin")
    else:
        print(f"#{i+1} Lose")
