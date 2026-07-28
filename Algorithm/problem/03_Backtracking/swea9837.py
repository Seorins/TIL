import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def recur(idx, cnt, total):
    global result

    if idx == 12:
        if cnt == N and total == K:
            result += 1 
        return 
        
    recur(idx+1, cnt+1, total + A[idx])
    recur(idx+1, cnt, total)

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]
    result = 0
    recur(0, 0, 0)

    print(f"#{tc} {result}")


