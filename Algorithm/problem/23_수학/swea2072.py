T = int(input())
result = []

for i in range(T):
    num_list = list(map(int, input().split()))
    odd_sum = 0

    for num in num_list:
        if num % 2 == 1:
            odd_sum += num

    result.append(f"#{i+1} {odd_sum}")

for r in result:
    print(r)
