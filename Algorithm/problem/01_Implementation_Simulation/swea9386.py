T = int(input())
result = []

for i in range(T):
    N = int(input())
    num_list = list(map(int, input()))
    cnt_list = [[]]

    for num in num_list:
        if num == 1:
            cnt_list[-1].append(num)

        else:
            cnt_list.append([])

    max_len = len(max(cnt_list))

    result.append(f"#{i+1} {max_len}")

for r in result:
    print(r)
