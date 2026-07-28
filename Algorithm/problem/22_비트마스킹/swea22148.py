T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = []

    while N != 0:
        result.append(N % 2)
        N//= 2
    
    cnt = 0
    for i in result:
        if i == 1:
            cnt += 1

    print(f"#{tc} {cnt}")