'''
1. 대각선 방향으로만 움직일 수 있음 [사각형모양]
(델타 -> 반시계방향 대각선 -> 무조건 한 번씩은 다 돌려야 함) 
2. 영역을 벗어나서는 안됨 (조건) 
3. 같은 숫자가 있으면 안됨 (조건) 
4. 하나의 카페에서만 먹는 것도 안됨 (1보단 커야 함) 
5. 왔던 길 돌아오는 것도 안됨 (visited 관리) 

디저트 최대한 많이 먹을 거임 냠

출발 => 임의의 한 카페 (for문으로 다 돌려야 함)
도착 => 원래 있던 자리로 돌아와야 함

# 디저트 못 먹으면 -1 출력
'''
# 시작 좌표와 다음 좌표가 같아지면 종료하게
def dfs(s_x, s_y, n_x, n_y, d, cnt, arr):
    global max_cnt

    # 반시계방향 대각선 
    di = [1, 1, -1, -1]
    dj = [-1, 1, 1, -1]

    for i in range(d, d+2):
        nx, ny = s_x + di[i], s_y + dj[i]
        

    # 종료 조건 
    if s_x == n_x and s_y == n_y:
        max_cnt = max(max_cnt, cnt)
        return 


    for c in range(1, N-1): # 대각선의 최대 횟수 
        for i in range(4):
            nx, ny = s_x + di[i]*c, s_y + dj[i]*c
            if graph[nx][ny] in arr:
                return False
            
            else: 
                if 0 <= nx < N and 0 <= ny < N :
                    arr.append(graph[nx][ny])
                    dfs(s_x, s_y, nx, ny, cnt+1, arr)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_cnt = 0

    for i in range(N):
        for j in range(N):
            dfs(i, j, -1, -1, 0, 1, [])


    # 마지막에 cnt가 여전히 1이면 경로가 없다는 거니까 -1 출력해줄거임
    if max_cnt == 1: max_cnt = -1

    print(f"#{tc} {max_cnt}")