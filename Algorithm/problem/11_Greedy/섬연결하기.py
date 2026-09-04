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