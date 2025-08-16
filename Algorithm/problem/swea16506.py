T = int(input())

def dfs(graph, v, target, visited):

    if v == target : 
        return True
    
    visited.add(v)

    for neighbor in graph[v]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
                
    return False

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {i : [] for i in range (1, V+1)}
    
    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)

    S, G = map(int, input().split())
    visited = set()

    result = 1 if dfs(graph, S, G, visited) else 0

    print(f"#{tc} {result}")