di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(cnt, idx, length):
    global max_cnt, min_len

    # 가지 치기
    # 남은 개수 + 지금까지 연결한 거 < 최대 개수 
    remain = len(core_lst) - idx
    if cnt + remain < max_cnt:
        return 
    
    # 종료 조건
    if idx == len(core_lst):
        if max_cnt < cnt:
            max_cnt = cnt
            min_len = length

        # 개수 같을 땐 길이 짧은 거
        elif max_cnt == cnt:
            min_len = min(min_len, length)

        return 
    
    x, y = core_lst[idx]

    # 현재 코어 연결 안 하는 경우
    dfs(cnt, idx+1, length)

    for c in range(4):
        nx, ny = x, y 
        movable = True
        path = []

        while True:
            nx += di[c]
            ny += dj[c]

            # 범위 벗어나면
            if nx < 0 or ny < 0 or nx >= N or ny >= N :
                break
            
            # core 있거나 이미 방문했을 경우
            if board[nx][ny] == 1 or visited[nx][ny] == 1:
                movable = False
                break

            path.append((nx, ny))

        if movable and path:
            
            for px, py in path:
                visited[px][py] = True

            dfs(cnt+1, idx+1, length+len(path))

            for px, py in path:
                visited[px][py] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_cnt = 0 # 최대 개수
    min_len = float('inf') # 최소 길이 

    core_lst = []
    # core 찾기
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                # 가장자리일 경우 그대로 패스 
                if i == 0 or j == 0 or i == N-1 or j == N-1:
                    visited[i][j] = 1
                    continue
                
                # list에 넣어서 dfs는 한 번만 돌리도록
                core_lst.append((i, j))

    dfs(0, 0, 0)
    
    print(f"#{tc} {min_len}")