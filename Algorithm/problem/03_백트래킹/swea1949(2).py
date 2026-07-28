'''
높은 봉우리에서 시작하여
상하좌우 방향으로만 이동 가능

- 현재 위치보다 낮은 지형으로만 이동 가능
- 같은 높이거나 더 높은 곳으로는 이동 불가
- 대각선 이동 불가

시작 지점은 반드시 가장 높은 봉우리여야 함

긴 등산로를 만들기 위해
딱 한 번 한 곳을 최대 K 깊이만큼 깎을 수 있음

가장 높은 봉우리들에서 각각 DFS 시작
'''

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(x, y, cnt, used_dig):
    global max_cnt
    visited[x][y] = True

    # 매번 갱신
    max_cnt = max(max_cnt, cnt)

    ch = graph[x][y]

    for k in range(4):
        nx = x + di[k]
        ny = y + dj[k]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny]:
            continue

        nh = graph[nx][ny]

        # 1. 그냥 이동 가능
        if ch > nh:
            dfs(nx, ny, cnt + 1, used_dig)

        # 2. 아직 안 깎았으면 한 번만 깎아서 이동
        elif used_dig == 0:
            need = nh - (ch - 1)  
            if 1 <= need <= K:
                original = graph[nx][ny]
                graph[nx][ny] = ch - 1
                dfs(nx, ny, cnt + 1, 1)
                graph[nx][ny] = original

    visited[x][y] = False


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_cnt = 0

    # 최고 봉우리 찾기
    max_h = max(map(max, graph))
    peaks = [(i, j) for i in range(N) for j in range(N) if graph[i][j] == max_h]

    # 각 봉우리에서 시작
    for sx, sy in peaks:
        dfs(sx, sy, 1, 0)

    print(f"#{tc} {max_cnt}")