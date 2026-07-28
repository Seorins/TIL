def solution(st):
    stack = []
    
    for s in st: 
        if s == '(' :
            stack.append('(')
            
        else :
            if not stack :  
                return False
            stack.pop()
    
    return not stack