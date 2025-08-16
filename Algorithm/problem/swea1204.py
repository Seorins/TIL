T = int(input())
result = []

for i in range(T):
    testcase = int(input())
    num_list = list(map(int, input().split()))
    max_cnt = 0
    max_index = 0
    num = num_list[0]

    for i in range(len(num_list)):
        

        if max_cnt <= cnt:
            max_cnt = cnt
            max_index = i

    result.append(f"#{i+1} {num_list[max_index]}")

for r in result:
    print(r)