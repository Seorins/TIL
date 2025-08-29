T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)

    for _ in range(M):
        x, y = map(int, input().split())
        arr[x] = y

    for i in range(N, 0, -1):
        if i*2 <= N:
            if i*2+1 <= N:
                arr[i] = arr[i*2] + arr[i*2+1]
            else:
                arr[i] = arr[i*2]

    print(f"#{tc} {arr[L]}")