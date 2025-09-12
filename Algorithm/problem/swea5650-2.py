'''
핀볼 게임판에 정사각형 블록 / 4가지 형태의 삼각형 블록 
+ 웜홀과 블랙홀 

* 어디에 만나냐에 따라 방향이 다름 (경사면 => 직각, 수평/수직 => 반대)
웜홀 : 6 ~ 10 
=> 웜홀에 빠지면 같은 숫자를 가진 다른 웜홀로 빠져나옴 (진행방향 유지) 쌍으로 주어짐
블랙홀 : -1 
=> 게임 끝

핀볼은 상하좌우 중 한 방향으로 움직임 (만나기 전까진 한 방향)

벽을 만나도 반대 방향으로 돌아옴 

게임 끝 => 출발 위치로 돌아오거나 / 블랙홀에 빠질 때 (종료)

점수 => 벽이나 블록에 부딪힌 횟수 (웜홀 통과 X)

최대 점수 

현재 d랑 블록이랑 관계에 대해서 파악 
'''
# d = 0위, 1오른, 2아래, 3왼
def dfs(sx, sy, d, cnt):
    global max_cnt
    x, y = sx, sy

    while True:

        # 시계방향
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1] 

        nx, ny = x + di[d], y + dj[d]

        if 0 <= nx < N and 0 <= ny < N :

            if (nx == sx and ny == sy) or (graph[nx][ny] == -1):
                max_cnt = max(max_cnt, cnt)
                return True
            
            # 그냥 갈 수 있는 경우 
            if graph[nx][ny] == 0:
                x, y = nx, ny

            # 만약 벽돌을 만난 경우 
            else : 
                # 웜홀 처리
                if 6 <= graph[nx][ny] and graph[nx][ny] <= 10 :
                    if pair[graph[nx][ny]][0] == (nx, ny):
                        nx, ny = pair[graph[nx][ny]][1]
                        x, y = nx, ny

                    else:
                        nx, ny = pair[graph[nx][ny]][0]
                        x, y = nx, ny

                # 일단 벽돌 처리
                # 경사면 기준
                # d가 0일땐 3, 2번 만나야 방향 바뀜 (3, 1)
                # d가 1일땐 3, 4번 만나야 방향 바뀜 (2, 0)
                # d가 2일땐 1, 4번 만나야 방향 바뀜 (1, 3)
                # d가 3일땐 1, 2번 만나야 방향 바뀜 (0, 2)

                elif d == 0:
                    if graph[nx][ny] == 3:
                        x, y = nx, ny
                        d = 3
                        cnt += 1

                    elif graph[nx][ny] == 2:
                        x, y = nx, ny
                        d = 1
                        cnt += 1

                    else:
                        x, y = nx, ny
                        d = 2
                        cnt += 1
                        
                elif d == 1:
                    if graph[nx][ny] == 3:
                        x, y = nx, ny
                        d = 2
                        cnt += 1

                    elif graph[nx][ny] == 4:
                        x, y = nx, ny
                        d = 0
                        cnt += 1

                    else:
                        x, y = nx, ny
                        d = 3
                        cnt += 1

                elif d == 2:
                    if graph[nx][ny] == 1:
                        x, y = nx, ny
                        d = 1
                        cnt += 1

                    elif graph[nx][ny] == 4:
                        x, y = nx, ny
                        d = 3
                        cnt += 1

                    else:
                        x, y = nx, ny
                        d = 0
                        cnt += 1

                elif d == 3:
                    if graph[nx][ny] == 1:
                        x, y = nx, ny
                        d = 0
                        cnt += 1

                    elif graph[nx][ny] == 2:
                        x, y = nx, ny
                        d = 2
                        cnt += 1

                    else:
                        x, y = nx, ny
                        d = 1
                        cnt += 1
                
        # 삐져 나왔을 떄 
        else:
            d = (d+2) % 4
            cnt += 1
            x, y = nx, ny
            continue

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    pair = {i:[] for i in range(6, 11)}
    max_cnt = 0

    # 시작할 수 있는 위치 : 0인 위치 
    for i in range(N):
        for j in range(N):
            # 웜홀 위치 찾기
            if 6 <=graph[i][j] <= 10:
                pair[graph[i][j]].append((i, j))


    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                for d in range(4):
                    # 출발 위치랑 진행 방향 임의기 때문에 일단 다 고려한다고 생각
                    dfs(i, j, d, 0)


    print(f"#{tc} {max_cnt}")