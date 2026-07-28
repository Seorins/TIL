from collections import deque 

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  
    user = list(map(int, input().split()))

    pizza = deque([i, user[i]] for i in range(M))

    oven = deque()
    for i in range(N):
        oven.append(pizza.popleft())

    while len(oven) > 1:
        num, cheese = oven.popleft()
        cheese //= 2

        if cheese == 0:
            if len(pizza) > 0:
                oven.append(pizza.popleft())

        else:
            oven.append((num, cheese))

    l_num, l_cheese = oven.popleft()

    print(f"#{tc} {l_num + 1}")

        