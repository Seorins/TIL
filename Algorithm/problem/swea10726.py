T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = []

    # 10진수를 2진수로 변환
    if M == 0:
        result = [0]
    else:
        while M != 0:
            result.append(M % 2)
            M //= 2
    
    while len(result) < N:
        result.append(0)

    switch = 'ON'
    for i in range(N):
        if result[i] != 1:
            switch = 'OFF'
            break

    print(f"#{tc} {switch}")