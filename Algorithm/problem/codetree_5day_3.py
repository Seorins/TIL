# 일단 틀린 코드임
# 다시 해야 해잇 열심히 했는데 .. ㅠㅠ

N = int(input())
sx, sy = map(int, input().split())
grid = [list(input()) for _ in range(N)]
x, y = sx-1, sy-1
cnt = 0

dir = 1 # 현재 방향
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 시계방향 # 발판은 그 다음 방향 거 보면 됨 


while True:

    # 다음 방향
    di, dj = direction[dir]
    nx, ny = x + di , y + dj
    
    # 다음 방향의 발판 유무
    b_di, b_dj = direction[(dir+1) % 4]
    b_nx, b_ny = nx + b_di, ny + b_dj

    if not (0 <= nx < N and 0 <= ny < N):
        cnt += 1
        break


    # 1. 앞이 격자 밖이면 탈출
    if not (0 <= nx < N and 0 <= ny < N):
        cnt += 1
        break


    # 2. 오른쪽에 벽이 있다면 그대로 전진
    if 0 <= b_nx < N and 0 <= b_ny < N and grid[b_nx][b_ny] == '#':
        if grid[nx][ny] != '#':
            x, y = nx, ny
            cnt += 1
        else:
            dir = (dir - 1) % 4  # 앞 막힘 → 반시계
        continue


    # 3. 오른쪽이 비어 있으면 시계방향 회전
    dir = (dir + 1) % 4


    # 방향 돌린 후 이동
    di, dj = direction[dir]
    nx, ny = x + di, y + dj
    if not (0 <= nx < N and 0 <= ny < N):
        cnt += 1
        break
    x, y = nx, ny
    cnt += 1


    # 시작 지점으로 돌아오면 종료
    if (x, y) == (sx - 1, sy - 1):
        cnt = -1
        break

print(cnt)
