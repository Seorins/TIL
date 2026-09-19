from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    dist = [-1] * (n+1)
    dist[1] = 0
    
    dq = deque([1])
    
    while dq:
        node = dq.popleft()
        
        for nxt_node in graph[node]:
            if dist[nxt_node] == -1:
                dist[nxt_node] = dist[node] + 1
                dq.append(nxt_node)
                
    max_num = max(dist)
    
    return dist.count(max_num)