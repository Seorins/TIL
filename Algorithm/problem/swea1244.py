import sys
sys.stdin = open('input.txt', 'r')

def dfs(cnt):
    global result

    if cnt == N:
        result = max(result, int("".join(number)))
        return

    for i in range(len(number)):
        for j in range(i+1, len(number)):
            number[i], number[j] = number[j], number[i]
            n_num = int("".join(number))

            if not visited[cnt][n_num]:
                visited[cnt][n_num] = True
                dfs(cnt + 1)
            number[i], number[j] = number[j], number[i]

T = int(input())
for tc in range(1, T+1):
    num, N = input().split()
    N = int(N)
    number = list(num)
    visited = [[False] * 1000000 for _ in range(N+1)]


    result = 0
    dfs(0)

    if N > len(number):
        if (N - len(number)) % 2 == 1:
            number[-1], number[-2] = number[-2], number[-1]
        result = max(result, int("".join(number)))

    print(f"#{tc} {result}")
