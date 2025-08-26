T = int(input())

for testcase in range(1, T + 1):
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]
    # N = 3 (부분집합의 원소의 수)
    # K = 6 (부분집합의 합)

    n_len = len(A)

    sum_cnt = 0

    for i in range(1 << n_len):
        bit_sum = 0
        cnt = 0
        for j in range(n_len):
            if i & (1 << j):
                bit_sum += A[j]
                cnt += 1
        if bit_sum == K and cnt == N:
            sum_cnt += 1

    print(f"#{testcase} {sum_cnt}")
