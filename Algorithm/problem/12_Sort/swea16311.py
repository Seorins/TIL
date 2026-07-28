T = int(input())

for testcase in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    new_numbers = []

    while len(numbers) > 0:
        new_numbers.append(max(numbers))
        new_numbers.append(min(numbers))

        numbers.remove(max(numbers))
        numbers.remove(min(numbers))

    print(f"#{testcase} {' '.join(map(str, new_numbers[:10]))}")
