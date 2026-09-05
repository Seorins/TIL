def solution(routes):
    
    routes.sort(key=lambda x: x[1])
    
    cnt = 0
    now = -30001
    
    for start, end in routes : 
        if now < start : 
            cnt += 1
            now = end
            
    return cnt