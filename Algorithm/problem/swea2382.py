'''
K개의 미생물 군집
N*N
가장자리에는 특수한 약품
1. 군집들은 1시간 마다 해당 방향으로 다음 셀 이동
2. 약품 셀에선 절반이 죽고 반대 방향으로 
3. 한 셀에서 마주치면 군집 합체 -> 미생물 수가 많은 군집의 방방향으로

=> M 시간 후의 미생물 총합 
'''

T = int(input())

for tc in range (1, T+1):
    N, M, K = map(int, input().split()) # 한 변 , 격리 시간, 군집 개수
    micro = [list(map(int, input().split())) for _ in range(K)]
    
    # 이동 방향 (상하좌우)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    reverse_dir = [2, 1, 4, 3]
    # 하나씩 조건 보면서 움직이기 
    for i in range(M):
        
        board = dict()
        
        for y, x, num, dir in micro:
            nx = x + dj[dir-1]
            ny = y + di[dir-1]
            
            # 약품 처리
            if ny == 0 or nx == 0 or nx == N-1 or ny == N-1:
                num //= 2
                dir = reverse_dir[dir-1]
                
            # 다 죽었을 때
            if num == 0:
                continue
            
            # board에 모으기
            if (ny, nx) not in board:
                board[(ny, nx)] = []
                
            board[(ny, nx)].append((num, dir))
            
            
        n_micro = []
        
        
        for key in board:
            
            y, x = key
            group = board[key]
            
            # 하나밖에 없을 때
            if len(group) == 1:
                num, dir = group[0]
                n_micro.append([y, x, num, dir])
                
            # 두 개 이상일 때
            else:
                total = sum(g[0] for g in group)
                
                max_num = group[0][0]
                max_dir = group[0][1]
                
                for g in group:
                    if g[0] > max_num:
                        max_num = g[0]
                        max_dir = g[1]
                        
                n_micro.append([y, x, total, max_dir])

        micro = n_micro
            
    result = 0
    for i in range(len(micro)):
        result += micro[i][2]
        
        
    print(f"#{tc} {result}")
                