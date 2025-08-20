from collections import deque

for _ in range(1, 11):
    tc = int(input())
    user = list(map(int, input().split()))
    numbers = deque(user)

    cycle = 0
    while True:
        num = numbers.popleft() - ((cycle % 5) + 1)
        cycle += 1
        if num <= 0:
            numbers.append(0)
            break
        else:
            numbers.append(num)

    print(f"#{tc}", *numbers)
    