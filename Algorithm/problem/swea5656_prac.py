import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

# 쏠 수 있는 횟수는 N번으로 한정 되어 있기 때문에 cnt 관리 해줘야 함
# 벽돌이 없으면 끝내줘야 해서 남은 벽돌도 관리 해줘야 함
# dfs를 하기 위해서는 복사본을 만들어서 깨는게 좋음
# 원본을 깨고 다시 원복하고 비효율적임
def shoot(cnt, remains, now_arr):
    global min_blocks

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 종료 조건 = N개의 구슬을 모두 발사하거나 남은 벽돌이 없을 때
    if cnt == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return
    
    # 한 줄씩 떨구기 
    for col in range(W):
        # [:] => 얕은 복사 방식 
        # 얕은 복사는 겉 리스트는 새로 만들지만, 안의 원소는 그대로 참조
        # 여기서 이렇게 해도 깊은 복사 효과가 나는 이유 ? 
        # row는 어차피 1차원 리스트이기때문에 겉껍데기만 복사해도 충분함 
        # 따라서 깊은 복사의 효과를 낼 수 있음 
        copy_arr = [row[:] for row in now_arr]

        # 가장 위 벽돌을 검색
        row = -1
        for r in range(H):
            if copy_arr[r][col]:
                row = r
                break
        
        # 벽돌이 없는 경우 
        if row == -1:
            continue

        # 숫자가 있는 젤 위에 거 넣음 
        dq = deque([(row, col, copy_arr[row][col])])
        now_remains = remains -1 # 넣고 나서 남은 벽돌 하나 없애주기 
        copy_arr[row][col] = 0 # 넣고나서 0으로 만들어주기 

        # 주변 벽돌들 파괴하기 
        while dq : 
            r, c, p = dq.popleft()
            for k in range(1, p):
                for i in range(4):
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)
                    
                    # 범위 밖이면 pass
                    if nr < 0 or nc < 0 or nr >= H or nc >= W:
                        continue
                    
                    # 벽돌이 없으면 pass
                    if copy_arr[nr][nc] == 0:
                        continue

                    dq.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc] = 0
                    now_remains -= 1
                    
        
        # 빈칸 메우기
        for c in range(W):
            idx = H -1
            for r in range(H-1, -1, -1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        shoot(cnt+1, now_remains, copy_arr)

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = float('inf') # 결론적으로 최소 벽돌 수를 구해야 함
    blocks = 0 # 가지치기 요소 (남은 벽돌 수가 없으면 자동적으로 종료시키기 위핵서)

    # 총 벽돌 수 세기
    for i in range(H):
        for j in range(W):
            if graph[i][j] : 
                blocks += 1

    # 나중에 전체 벽돌 수에서 하나하나 없애줄 거임 

    shoot(0, blocks, graph)
    print(f"#{tc} {min_blocks}")