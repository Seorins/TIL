N, M = map(int, input().split())
arr = []

def recur(num):

    if num == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if i in arr:
            continue
        if arr and arr[-1] > i :
                continue
        arr.append(i)
        recur(num+1)
        arr.pop()


recur(0)
