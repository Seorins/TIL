# 0위, 1아래, 2왼, 3오 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 튕긴 후 방향
change_dir = {
    1: [1, 3, 0, 2],
    2: [3, 0, 1, 2],
    3: [2, 0, 3, 1],
    4: [1, 2, 3, 0],
    5: [1, 0, 3, 2],
}

def dfs(sx, sy, d, cnt):
    global max_cnt
    x, y = sx, sy

    while True:
        nx, ny = x + dx[d], y + dy[d]

        # 방향 반전 + 점수 +1
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            d ^= 1
            cnt += 1
            x, y = nx, ny   
            continue

        val = graph[nx][ny]

        # 시작점 복귀 / 블랙홀
        if (nx == sx and ny == sy) or val == -1:
            max_cnt = max(max_cnt, cnt)
            return

        # 빈칸
        if val == 0:
            x, y = nx, ny
            continue

        # 웜홀
        if 6 <= val <= 10:
            a, b = pair[val][0]
            c, d2 = pair[val][1]
            if (nx, ny) == (a, b):
                x, y = c, d2
            else:
                x, y = a, b
            continue

        # 블록(1~5)
        # 방향 바꾸고 +1점, 그 칸으로 이동
        d = change_dir[val][d]
        cnt += 1
        x, y = nx, ny


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    pair = {i: [] for i in range(6, 11)}
    max_cnt = 0

    for i in range(N):
        for j in range(N):
            if 6 <= graph[i][j] <= 10:
                pair[graph[i][j]].append((i, j))

    # 모든 빈칸에서 4방향 시작
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                for d in range(4):
                    dfs(i, j, d, 0)

    print(f"#{tc} {max_cnt}")
