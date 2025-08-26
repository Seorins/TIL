# 필요한 거 그래프, 처음, 목표, 방문
def dfs(graph, start, end, visited):
    
    if start == end :
        return True
    
    visited.add(start)

    for node in graph[start]:
        if node not in visited:
            if dfs(graph, node, end, visited):
                return True
    
    return False


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {i:[] for i in range(1, V+1)}
    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
    S, G = map(int, input().split())

    visited = set()
    
    result = 0
    if dfs(graph, S, G, visited) : 
        result = 1
    
    print(f"#{tc} {result}")

