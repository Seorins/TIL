# kruskal

def solution(n, costs):

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        
        if a == b : 
            return False
        
        parent[b] = a
        return True

    parent = list(range(n))
    
    costs.sort(key = lambda x:x[2])
    
    answer = 0
    
    for a, b, cost in costs : 
        if union(a, b):
            answer += cost
            
    return answer


# --------------------------------------------

# prim

import heapq

def solution(n, costs):
    
    graph = [[] for _ in range(n)]
    
    for x, y, cost in costs: 
        graph[x].append((cost, y))
        graph[y].append((cost, x))
        
    visited = [False] * n
    
    heap = [(0, 0)]
    
    answer = 0
    
    while heap: 
        cost, node = heapq.heappop(heap)
        
        if visited[node]: 
            continue
            
        visited[node] = True
        answer += cost
        
        for nxt_cost, nxt_node in graph[node]:
            if not visited[nxt_node]:
                heapq.heappush(heap, (nxt_cost, nxt_node))
                
    return answer