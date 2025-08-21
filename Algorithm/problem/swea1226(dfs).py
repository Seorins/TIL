# dfs 풀이
def dfs(graph, x, y, visited) :

    if graph[x][y] == 3:
        return True
    
    visited[x][y] = True

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for t in range(4):
        dx = x + di[t]
        dy = y + dj[t]
        if 0 <= dx < 16 and 0 <= dy < 16:
            if not visited[dx][dy] and graph[dx][dy] != 1:
                if dfs(graph, dx, dy, visited):
                    return True
    return False

for _ in range(1, 11):
    tc  = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    # 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

    x = y = 1
    result = 0
    
    if dfs(graph, x, y, visited):
        result = 1

    print(f"#{tc} {result}")