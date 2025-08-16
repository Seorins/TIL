T = int(input())
result = []

for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    max_num = num_list[0]
    min_num = num_list[0]

    for num in num_list:
        if max_num < num:
            max_num = num

    for num in num_list:
        if min_num > num:
            min_num = num

    minus_num = max_num - min_num

    result.append(f"#{i+1} {minus_num}")

for r in result:
    print(r)
