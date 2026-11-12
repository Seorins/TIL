def solution(s):
    # O(N^2)까지 가능 
    # 실제 회전 X -> index로 생각
    cnt = 0
    n = len(s)
    
    for i in range(n):
        stack = []
        for j in range(n):
            now = s[(i+j) % n]
            
            if now in ("(", "[", "{"):
                stack.append(now)
                
            else: 
                if not stack:
                    break
                    
                if now == ")" and stack[-1] == "(":
                    stack.pop()
                    
                elif now == "]" and stack[-1] == "[":
                    stack.pop()
                
                elif now == "}" and stack[-1] == "{":
                    stack.pop()
                    
                else:
                    break
                    
        else:    
            if not stack:
                    cnt += 1
                    
    return cnt