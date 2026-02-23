'''
1. 대각선 방향으로만 움직일 수 있음 [사각형모양]
(델타 -> 반시계방향 대각선) 
2. 영역을 벗어나서는 안됨 (조건) 
3. 같은 숫자가 있으면 안됨 (조건) 
4. 하나의 카페에서만 먹는 것도 안됨 (1보단 커야 함) 
5. 같은 디저트 번호를 다시 먹으면 안 됨

디저트 최대한 많이 먹을 거임

# 가능한 투어가 하나도 없으면 -1 출력
'''
di = [1, 1, -1, -1]
dj = [-1, 1, 1, -1]

def dfs(sx, sy, x, y, d, cnt, arr):
    global max_cnt

    # 현재 방향에서 직진 또는 꺾기만
    for nd in (d, d + 1):
        if nd >= 4:
            continue

        nx = x + di[nd]
        ny = y + dj[nd]

        # 시작점으로 복귀
        if nx == sx and ny == sy:
            if cnt >= 4: # 사각형 최소 길이 보장
                max_cnt = max(max_cnt, cnt)
            continue

        # 범위 체크
        if not (0 <= nx < N and 0 <= ny < N):
            continue

        # 디저트 중복 체크
        if graph[nx][ny] in arr:
            continue

        arr.append(graph[nx][ny])
        dfs(sx, sy, nx, ny, nd, cnt + 1, arr)
        arr.pop()


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = -1

    for i in range(N - 2):
        for j in range(1, N - 1):
            # 시작점 디저트는 처음부터 먹고 시작
            dfs(i, j, i, j, 0, 1, [graph[i][j]])

    print(f"#{tc} {max_cnt}")