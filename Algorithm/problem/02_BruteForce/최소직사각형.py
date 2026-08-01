def solution(sizes):
    w = 0
    h = 0
    
    for x, y in sizes : 
        w = max(w, max(x, y))
        h = max(h, min(x, y))
        
    return w*h