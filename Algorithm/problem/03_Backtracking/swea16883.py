T = int(input())

def recur(x, y, cnt):
    global min_cnt

    if min_cnt < cnt :
        return 

    if x == N-1 and y == N-1 :
        min_cnt = min(min_cnt, cnt) 
        return 

    for di, dj in [[1, 0], [0, 1]]:
        nx, ny = x + di, y + dj
        if 0 <= nx < N and 0 <= ny < N : 
            recur(nx, ny, cnt + graph[nx][ny])


for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    min_cnt = float('inf')

    recur(0, 0, graph[0][0])

    print(f"#{tc} {min_cnt}")

