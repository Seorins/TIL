T = int(input())

for tc in range(1, T+1):
    N = int(input()) # Command 수
    dist = 0
    now = 0

    # 0 유지 1 가속 2 감속 
    # 2번째 자리는 (가)속도

    for _ in range(N):
        command = list(map(int, input().split()))

        if command[0] == 0:
            dist += now

        elif command[0] == 1:
            now += command[1]
            dist += now

        elif command[0] == 2:
            now -= command[1]
            if now < 0 :  
                now = 0 

            dist += now

    print(f'#{tc} {dist}')
