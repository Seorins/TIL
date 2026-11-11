def is_valid(x, y):
    return -5 <= x <= 5 and -5 <= y <= 5

def move(x, y, dir):
    if dir == 'U':
        nx, ny = x, y+1
    elif dir == 'D':
        nx, ny = x, y-1
    elif dir == 'R':
        nx, ny = x+1, y
    else:
        nx, ny = x-1, y 
    return nx, ny

def solution(dirs):
    x, y = 0, 0
    ans = set()
    
    for dir in dirs:
        nx, ny = move(x, y, dir)
        
        if not is_valid(nx, ny):
            continue
            
        ans.add((x, y, nx, ny))
        ans.add((nx, ny, x, y))
        x, y = nx, ny
       
    return len(ans) // 2