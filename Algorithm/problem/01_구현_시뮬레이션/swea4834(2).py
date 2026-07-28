T = int(input())
result = []

for i in range(T):
    N = int(input())
    nums = list(map(int, input()))

    num_list = [0] * 10

    for num in nums:
        num_list[num] += 1  

    max_num = 0
    max_cnt = 0
    for num in range(len(num_list)):
        if max_cnt <= num_list[num]:
            max_cnt = num_list[num]
            max_num = num

    result.append(f"#{i+1} {max_num} {max_cnt}")

for r in result:
    print(r)
