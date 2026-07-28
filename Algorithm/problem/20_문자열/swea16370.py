T = int(input())

for testcase in range(1, T + 1):
    N = input()  # XYPV
    M = input()  # EOGGXYPVSY

    max_cnt = 0
    for char in N:
        cnt = M.count(char)

        if max_cnt < cnt:
            max_cnt = cnt

    print(f"#{testcase} {max_cnt}")
