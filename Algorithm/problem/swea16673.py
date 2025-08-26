from collections import deque

def bfs(graph, S, G):
    visited = [False] * (len(graph)+1)
    dist = [0] * (len(graph)+1)
    dq = deque([S])
    visited[S] = True

    while dq:
        v =  dq.popleft()

        if v == G : 
            return dist[G] 

        for next in graph[v] :
            if not visited[next]:
                dq.append(next)
                visited[next] = True 
                dist[next] = dist[v] + 1        
    return 0
    
T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {i:[] for i in range(1, V+1)}

    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    S, G = map(int, input().split())

    print(f"#{tc} {bfs(graph, S, G)} ")
