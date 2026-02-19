'''
가장 위의 벽돌이 맞고 그 숫자-1만큼 옆에 있는 사방에 있는 벽돌 깨짐
또 맞은 벽돌이 영향을 받고 그만큼 깨짐 (2 이상부터)
그리고 빈 공간이 있으면 내려옴

N개의 벽돌을 떨어트려 최대한 많은 벽돌 제거 

젤 위에 있는 벽돌을 찾고
깨고.. 내리고..

-> 원본 건드리지 말고 복사해서 쓰기

필요한 기능
위에 블록 찾기
깨트리기 -> 밑으로 내리기 
'''

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def shoot(cnt, remain, now):
    global min_block

    # 종료조건 -> 블록 없을 때, shoot 기회 다 썼을 때
    if cnt == N or remain == 0:
        min_block = min(min_block, remain)
        return 

    # 열마다 하나씩 깨트리기 
    for col in range(W):
        
        # 복사하고 시작
        copy_board = [row [:] for row in now]
        
        row = -1
        
        # 젤 위에 있는 거 찾기 
        for r in range(H):
            if copy_board[r][col]:
                row = r
                break
            
        # 열에 벽돌이 없을 때
        if row == -1:
            continue
        
        # 이제 정해진 벽돌부터 BFS 돌리기 
        dq = deque([(row, col, copy_board[row][col])])
        now_remain = remain - 1
        copy_board[row][col] = 0
        
        
        while dq: 
            r, c, num = dq.popleft()
            
            for i in range(4):
                for k in range(1, num):
                    nr = r + dy[i] * k
                    nc = c + dx[i] * k
                        
                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue
                    
                    if copy_board[nr][nc] == 0:
                        continue
                    
                    dq.append((nr, nc, copy_board[nr][nc]))
                    copy_board[nr][nc] = 0
                    now_remain -= 1
                    
        # 빈칸 채우기 idx로 빈 곳 기억하고 해당 장소로 옮기기 
        for c in range(W):
            idx = H-1
            for r in range(H-1, -1, -1):
                if copy_board[r][c]:
                    copy_board[r][c], copy_board[idx][c] = copy_board[idx][c], copy_board[r][c]
                    idx -= 1
                
        shoot(cnt+1, now_remain, copy_board)
                
        
    
T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    min_block = float('inf')
    remain = 0 # 남은 벽돌 수 기록 
    
    # 벽돌 수 세기 
    for i in range(H):
        for j in range(W):
            if board[i][j] :
                remain += 1
                
    
    shoot(0, remain, board)
    
    print(f"#{tc} {min_block}")