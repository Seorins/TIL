import sys
sys.stdin = open("input.txt", 'r')
'''
N*N 격자판이 있음
한 칸에는 1개의 core 혹은 1개의 전선이 올 수 있음
가장자리에는 전원이 흐르고 있음

전선은 직선으로만 가능! 교차는 안됨! 가장자리는 이미 전원 연결!

* 최대한 많이 연결했을 때 전선 길이의 합을 구하시오 
* 단 여러 방법이 있을 경우엔 전선 길이의 합이 최소가 되는 것 구하기
* 최대한 많이 해도 전원 연결이 안되는 core도 있을 수 있음 

i) DFS + 백트래킹 ? 
'''

# 인덱스로 리스트에 하나씩 접근해보기 ? 
# [(1, 2), (2, 5), (4, 1), (4, 3), (5, 1)]
def dfs(idx, cnt, length):
    global max_cnt, min_len

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 이제 core리스트 다 돌았다는 거 (종료조건)
    if idx == len(core_lst):
        if max_cnt < cnt:
            max_cnt = cnt
            min_len = length
        # 그런데 이제 여러 방법이 있으면 최소로 해줘야 함
        elif max_cnt == cnt:
            min_len = min(min_len, length)

        return 

    # 그럼 이제 한 방향씩 직진으로 놓아보기
    # 근데 앞에 뭐가 있으면 돌아와야 함
    x, y = core_lst[idx]
    # print(x, y)

    for c in range(4):
        nx, ny = x, y
        movable = True
        path = []

        while True : 
            nx += di[c]
            ny += dj[c]

            # 여기까지 왔다는 것은 전원이 연결됐다는 것 
            if nx < 0 or ny < 0 or nx >= N or ny >= N :
                break

            # 가다가 core가 있으면 나갈거임 
            if graph[nx][ny] != 0 :
                movable = False
                break

            path.append((nx, ny))
        
        # 이제 가는 길에 뭐가 없다는 것을 확인함! 
        # 그럼 한 번 진짜로 깔아볼까?
        if movable:
            
            for x, y in path:
                visited[x][y] = True

            dfs(idx+1, cnt+1, length+len(path))
            
            for x, y in path:
                visited[x][y] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_cnt = 0 # 최대 코어
    min_len = float('inf') # 만약 개수가 같으면 최소 길이로 해야 함

    # 일단 core가 있는 좌표를 찾아보자
    core_lst = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                if i == 0 or j== 0 or i == N-1 or j == N-1 :
                    continue
                core_lst.append((i, j))

    # core 여러 개 있는 거 동시에 다 처리해줘야하니까
    # 그냥 일반적으로 for문 돌려서 함수호출 하면 안될 거 같음

    dfs(0, 0, 0)

    print(f"#{tc} {min_len}")

