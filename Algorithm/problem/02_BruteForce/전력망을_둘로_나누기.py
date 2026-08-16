def solution(n, wires):
    tree = [[] for _ in range(n+1)]
    
    for a, b in wires : 
        tree[a].append(b)
        tree[b].append(a)
        
    answer = n
    
    # a, b를 끊었다 가정
    for a, b in wires : 
        visited = [False] * (n+1)
        stack = [1]
        visited[1] = True 
        cnt = 0
        
        while(stack):
            node = stack.pop()
            cnt += 1
            
            for nxt_node in tree[node]:
                # 끊어진 길이면 패스 
                if (node == a and nxt_node == b) or (node == b and nxt_node == a) : 
                    continue
                   
                if not visited[nxt_node]:
                    visited[nxt_node] = True
                    stack.append(nxt_node)
                    
        diff = abs(cnt - (n - cnt))
        answer = min(answer, diff)
        
    return answer
            
                