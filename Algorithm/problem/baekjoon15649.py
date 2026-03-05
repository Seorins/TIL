# 1부터 N까지의 자연수 중에서 중복 없이 M개를 고른 수열
def recur(idx):

    # 종료 조건
    if idx == M :
        print(*arr)

    for i in number:
        if i in arr:
            continue
    
        arr.append(i)
        recur(idx+1)
        arr.pop()

    
N, M = map(int, input().split())
number = [i for i in range(1, N+1)]
arr = []


recur(0)