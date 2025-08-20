# 1부터 N까지의 자연수 중에서 중복 없이 M개를 고른 수열
N, M = map(int, input().split())
number = [i for i in range(1, N+1)]
arr = []

def recur(num):

    if num == M:
        print(*arr)
        return
    
    for i in number:
        if i in arr:
            continue

        arr.append(i)
        recur(num+1)
        arr.pop()

recur(0)