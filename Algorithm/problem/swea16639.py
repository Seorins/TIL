from collections import deque 

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) 
    # N 개를 동시에 구울 수 있음
    # M개의 피자를 구워야 함 
    pizza = list(map(int, input().split()))
    # 7 2 6 5 3

    bake = deque(maxlen=N)

    for i in range(M):
        deque.
