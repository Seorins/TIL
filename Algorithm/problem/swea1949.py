import sys, os
BASE_DIR = os.path.dirname(__file__)  
sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")

'''
원래는 낮은곳에서 높은 곳으로 가야함 (가로, 세로만 가능)
안되는 것 X = 높이가 같거나 더 낮은 지형으로 가는 것, 대각선은 불가능함
 
단, 시작지점이 가장 높은 봉우리에서 시작해야 함!
그럼 높은 곳에서 낮은 곳으로 차례대로 보면 될 거 같음
* 움직일 때마다 현재 위치를 저장할 필요가 있을 듯 

긴 등산로를 만들기 위해 딱 한 곳을 정해서 K 깊이만큼 지형을 깎을 수 있음
이렇게 되면 1~K만큼 마음대로 깎을 수 있음 (필요한 경우)

그러면 최대 공사 가능 깊이가 K일 때,
0부터 ~ K까지 깎는 경우를 다 탐색해야 함

어떻게 ? 땅파기를 사용했는지 여부에 따라서 사용을 안했으면 추가로 사용하는 분기 활용 

풀이 : dfs 사용해서 시도
'''

def dfs(x, y, cnt, dig):
    global max_cnt
    visited[x][y] = True
    movable = False # 움직일 수 있는지 관리 (종료 조건)

    # 상하좌우 갈 수 있음
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for c in range(4):
        dx = x + di[c]
        dy = y + dj[c]

        # out of range 둘 다 떠서 공통으로 빼버림
        if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy]:
        
            # i) 그냥 갈 수 있는 경우 
            if graph[x][y] > graph[dx][dy]:
                movable = True
                dfs(dx, dy, cnt+1, dig)

            # ii) 땅 파기를 활용해야 하는 경우 
            elif not dig :
                for d in range(1, K+1):
                    if graph[dx][dy] - d < graph[x][y]:
                        graph[dx][dy] -= d
                        movable = True
                        dfs(dx, dy, cnt + 1, 1)
                        # 백트래킹 
                        graph[dx][dy] += d

    # 끝에 도달하면 길이 반영
    if not movable:
        max_cnt = max(max_cnt, cnt)

    # 백트래킹 실시 
    visited[x][y] = False


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]* N for _ in range(N)]
    cnt = 1 
    max_cnt = dig = 0

    # 가장 높은 봉우리 찾기(시작점)
    max_m = max(map(max, graph))

    # print(max_m)

    # 가장 높은 봉우리가 한 좌표가 아닐 수 있음 
    # 따라서 해당 봉우리가 있는 좌표를 모두 찾음 
    m_lst = [] # 꼭대기 좌표 모음
    for i in range(N):
        for j in range(N):
            if graph[i][j] == max_m:
                m_lst.append((i, j)) 

    # print(m_lst)

    # 이제 해당 좌표를 가지고 가장 긴 등산로를 찾아야 함 
    # 그 전에 k 깎는 것을 어떻게 할 것인가? 
    # 땅파기를 사용했는지 여부에 따라서 사용을 안했으면 추가로 사용하는 분기 활용 

    # 높은 곳마다 호출해보기
    for x, y in m_lst:
        dfs(x, y, cnt, dig)

    print(f"#{tc} {max_cnt}")