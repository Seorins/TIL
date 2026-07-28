from collections import deque 

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))
    q = [0] * N

    front = rear = -1

    for i in number:
        rear = (rear+1) % N
        q[rear] = i

    for _ in range(M):
        front = (front + 1) % N
        v = q[front]
        
        rear = (rear +1 ) % N
        q[rear] = v

    print(f"#{tc} {q[(front+1) % N]}")