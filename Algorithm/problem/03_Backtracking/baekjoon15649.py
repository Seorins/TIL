# 1부터 N까지의 자연수 중에서 중복 없이 M개를 고른 수열
def recur(depth):

    if depth == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if visited[i]:
            continue

        visited[i] = True
        arr.append(i)

        recur(depth + 1)

        arr.pop()
        visited[i] = False


N, M = map(int, input().split())

arr = []
visited = [False] * (N+1)

recur(0)