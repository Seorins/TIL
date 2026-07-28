def check(idx, color):
    for i in graph[idx]:
        if colors[i] == color:
            return False
    return True

def dfs(idx):
    
    if idx > N : 
        return 1
    
    for i in range(1, M+1):
        if check(idx, i):
            colors[idx] = i

            if dfs(idx+1):
                return 1
            colors[idx] = 0
    return 0

T = int(input())

for tc in range(1, T+1):
    # N = 노드 개수 E = 간선 개수 M = 색상 수
    N, E, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    colors = [0] * (N+1)

    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    print(f"#{tc} {dfs(1)}")

    