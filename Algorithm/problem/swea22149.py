T = int(input())

for tc in range(1, T+1):
    N = int(input())
    people = list(map(int, input().split()))

    result = 0
    for p in people :
        result ^= p

    print(f"#{tc} {result}")