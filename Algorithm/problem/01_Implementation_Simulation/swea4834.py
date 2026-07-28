T = int(input())
result = []

for i in range(T):
    N = int(input())
    nums = list(map(str, input()))
    nums.sort()
    str_nums = "".join(nums)
    max_cnt = 0
    max_num = 0

    # 46799

    for num in str_nums:
        cnt = str_nums.count(num)
        if max_cnt <= cnt:
            max_cnt = cnt
            max_num = int(num)

    result.append(f"#{i+1} {max_num} {max_cnt}")

for r in result:
    print(r)
