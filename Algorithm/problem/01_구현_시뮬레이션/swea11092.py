T = int(input())
result = []

for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    max_num = num_list[0]
    max_idx = 0
    min_num = num_list[0]
    min_idx = 0

    for j in range(len(num_list)):

        if max_num <= num_list[j]:
            max_num = num_list[j]
            max_idx = j

        if min_num > num_list[j]:
            min_num = num_list[j]
            min_idx = j

    minus_idx = abs(max_idx - min_idx)

    result.append(f"#{i+1} {minus_idx}")

for r in result:
    print(r)
