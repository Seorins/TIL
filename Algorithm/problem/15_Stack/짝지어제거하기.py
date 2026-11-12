def solution(s):
    # O(NlogN)까지도 가능
    stack = []
    
    for st in s:
        if not stack :
            stack.append(st)
            
        elif stack[-1] == st:
            stack.pop()
            
        else:
            stack.append(st)
            
    return(1 if not stack else 0)
    