T = 10
result = []

for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    view_sum = 0
    left = 0
    right = 0

    for j in range(2, N - 2):
        left = max(num_list[j - 2], num_list[j - 1])
        right = max(num_list[j + 2], num_list[j + 1])

        if num_list[j] - left > 0 and num_list[j] - right > 0:
            view_sum += min((num_list[j] - left), (num_list[j] - right))

    result.append(f"#{i+1} {view_sum}")

for r in result:
    print(r)
