from collections import deque 

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))
    
    q = deque(number)
    q.rotate(-M)

    print(f"#{tc} {q[0]}")