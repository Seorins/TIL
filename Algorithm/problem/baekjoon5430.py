from collections import deque

T = int(input())

for _ in range(1, T+1):
    p = input()
    n = int(input())
    arr = input()[1:-1]

    if arr : 
        dq = deque(map(int, arr.split(',')))
    else:
        dq = deque()

    revs = False
    error = False

    for i in p:
        if i == 'R':
            revs = not revs
        
        else:
            if not dq:
                print("error")
                error = True
                break
            
            if revs:
                dq.pop()

            else:
                dq.popleft()

    if not error:
        if revs:
            dq.reverse()
        print(f"[{','.join(map(str, dq))}]")