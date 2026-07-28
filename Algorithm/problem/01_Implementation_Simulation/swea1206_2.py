T = 10
result = []

for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    view_sum = 0
    left = 0
    right = 0

    for j in range(2, N - 2):

        if num_list[j - 2] > num_list[j - 1]:
            left = num_list[j - 2]
        else:
            left = num_list[j - 1]

        if num_list[j + 2] > num_list[j + 1]:
            right = num_list[j + 2]
        else:
            right = num_list[j + 1]

        if num_list[j] - left > 0 and num_list[j] - right > 0:
            if (num_list[j] - left) > (num_list[j] - right):
                view_sum += num_list[j] - right

            else:
                view_sum += num_list[j] - left

    result.append(f"#{i+1} {view_sum}")

for r in result:
    print(r)
