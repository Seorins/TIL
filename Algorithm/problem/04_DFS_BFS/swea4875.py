T = int(input())

def dfs(graph, start_x, start_y, visited, end):
    
    if graph[start_x][start_y] == end : 
        return 1
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    visited[start_x][start_y] = True

    N = len(graph)

    for t in range(4):
        dx = start_x + di[t]
        dy = start_y + dj[t]
        if 0 <= dx < N and 0 <= dy < N and graph[dx][dy] != 1 and not visited[dx][dy]:
            if dfs(graph, dx, dy, visited, end):
                return 1
    return 0
    
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    start_x = start_y = -1

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                start_x = i
                start_y = j

    end = 3
    result = dfs(graph, start_x, start_y, visited, end)
    
    print(f"#{tc} {result}")

