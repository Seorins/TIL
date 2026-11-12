from collections import deque

def solution(N, K):
    dq = deque(range(1, N+1))

    while len(dq) > 1:
        for _ in range(K-1):
            dq.append(dq.popleft())

        dq.popleft()
    return dq[0]

