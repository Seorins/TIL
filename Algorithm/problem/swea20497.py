T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())
    rocks = list(map(int, input().split()))

    for i in range(M):
        i, j = map(int, input().split())

        for c in range(1, j+1):
            if 0<=i-1-c<N and 0 <= i-1+c <N:
                if rocks[i-1-c] == 0 and rocks[i-1+c] == 0:
                    rocks[i-1-c] = 1
                    rocks[i-1+c] = 1

                elif rocks[i-1-c] == 1 and rocks[i-1+c] == 1:
                    rocks[i-1-c] = 0
                    rocks[i-1+c] = 0

    print(f"#{testcase}", *rocks)