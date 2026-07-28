T = int(input())

for tc in range(1, T+1):
    N = int(input())
    node = list(map(int, input().split()))
    result = True

    i = 0
    while (2 ** i) <= N:
        start = (2 ** i) -1
        k = 2 ** i
        part = node[start:start+k]
        if part != part[::-1]:
            result = False
            break
        i += 1

    print(f"#{tc} {result}")