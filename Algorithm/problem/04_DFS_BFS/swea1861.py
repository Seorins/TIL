'''
위에서 i번째 줄의(행) / 왼쪽에서 j번째 방(열)에는 
1이상 N^2 이하의 수 Ai,j가 적혀 있으며 상하좌우 다른 방 이동 가능
이동하려는 방 존재, 현재 방보다 정확히 1 커야함
 
처음에 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있음 ? 
 
처음 출발해야하는 방 번호 => graph[i][j] / 최대 몇개의 방 (본인 포함)
'''
 
def dfs(x, y, cnt, room):
    global max_len, min_room
 
    movable = False
    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx, ny = x + di, y + dj
        if 0 <= nx < N and 0 <= ny < N :
            if graph[x][y] == graph[nx][ny] -1:
                movable = True
                dfs(nx, ny, cnt + 1, room)  
             
    if not movable:
        if cnt > max_len or (cnt == max_len and room < min_room):
            max_len = cnt
            min_room = room
 
         
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0
    min_room = float('inf') 
 
    for i in range(N):
        for j in range(N):
            dfs(i, j, 1, graph[i][j])
 
    print(f"#{tc} {min_room} {max_len}")