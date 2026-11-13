def get_path(points, routes):
    path = []
    
    # 시작 좌표
    start_r, start_c = points[routes[0]-1][0], points[routes[0]-1][1]
    path.append((start_r, start_c))
    
    # 시작 좌표 후부터 이동
    for i in range(1, len(routes)):
        end_r, end_c = points[routes[i]-1][0], points[routes[i]-1][1]
        # r부터 이동
        while start_r != end_r:
            start_r += 1 if end_r > start_r else -1
            path.append((start_r, start_c))
        
        # c 이동 
        while start_c != end_c:
            start_c += 1 if end_c > start_c else -1
            path.append((start_r, start_c))
    
    return path

def solution(points, routes):
    paths = []
    ans = 0
    
    for route in routes:
        paths.append(get_path(points, route))
    
    # 가장 긴 길이 기준으로 확인 
    max_path = max(len(path) for path in paths)
    
    # 같은 시간끼리 모으기
    for t in range(max_path):
        positions = {}
        
        for path in paths:
            if t < len(path):
                pos = path[t]
                positions[pos] = positions.get(pos, 0) + 1
        
        # 충돌 상황 계산
        for cnt in positions.values():
            if cnt > 1:
                ans += 1
                
    return ans
        
    