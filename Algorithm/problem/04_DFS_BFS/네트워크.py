# DFS

def solution(n, computers):
        
    visited = [False] * n
        
    def dfs(i) :
        visited[i] = True
        
        for j in range(n):
            if computers[i][j] == 1 and not visited[j] : 
                dfs(j)
        return 
        
    cnt = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    return cnt
        
# ------------------------------------------------------------

# BFS

from collections import deque

def solution(n, computers):
        
    visited = [False] * n
    
    def bfs(i): 
        dq = deque()
        dq.append(i)
        visited[i] = True
        
        while dq: 
            node = dq.popleft()
            
            for j in range(n): 
                if computers[node][j] == 1 and not visited[j]:
                    visited[j] = True
                    dq.append(j)
            
    cnt = 0 
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1    
        
    return cnt    

# ------------------------------------------------------------

# UNION FIND

def solution(n, computers):
        
    parents = [i for i in range(n)]
    
    def find(x): 
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        
        if a == b: 
            return False
        
        parents[b] = a
        
        return True
        
    for i in range(n): 
        for j in range(i+1, n):
            if computers[i][j] == 1:
                union(i, j)
                
    for i in range(n):
        find(i)
        
    return len(set(parents))