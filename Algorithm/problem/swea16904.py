import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    times = []
    for i in range(N):
        s, e = map(int, input().split())
        times.append([s, e])

    # 종료 시간이 빠른 순서대로
    times.sort(key=lambda x:x[1])
    # print(times)

    cnt = 0
    end = 0
    
    for s, e in times:
        if s >= end:
            cnt += 1
            end = e

    print(f'#{tc} {cnt}')

