T = int(input())

for i in range(T):

    testcase = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()

    len_list = [[]]
    max_len = 0
    num = num_list[0]

    for j in len_list:
        if num == j:
            len_list.append(num)
            num = j

        else:
            len_list.append([])
            len_list.append(num)
            num = j

    