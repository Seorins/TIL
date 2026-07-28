T = int(input())
result = []

for i in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    max_sum = 0
    min_sum = sum(num_list)

    for j in range(N - M + 1):
        origin_sum = 0
        for k in range(M):
            origin_sum += num_list[k + j]

        if max_sum < origin_sum:
            max_sum = origin_sum

        if min_sum > origin_sum:
            min_sum = origin_sum

    minus_sum = max_sum - min_sum

    result.append(f"#{i+1} {minus_sum}")

for r in result:
    print(r)
