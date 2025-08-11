T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))

    cnt= 0
    for i in range(N):
        if before[i] != after[i]:
            cnt += 1
            for j in range(i, N):
               before[j] = 1 - before[j]

    print(f"#{testcase} {cnt}")