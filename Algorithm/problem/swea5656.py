import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

'''
1. 구슬은 좌, 우로만 움직일 수 있음 
-> 맨 위 벽돌만 깰 수 있음

2. 벽돌은 숫자 1~9 
명중하면 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거

3. 제거되는 범위 내에 있는 벽돌은 동시에 제거 

-> 제거될 때 같이 제거 당하는 벽돌의 해당 숫자만큼 또 제거됨 !!!

-> 제거되면 나머지는 밑으로 떨어짐 

* 최소 벽돌
- 현재 벽돌이 다 깨지면 더 이상 할 필요가 없다 -> 현재 벽돌 수 관리
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def shoot(cnt, remains, now_arr):
    global min_blocks

    # 종료 조건, N개의 구슬을 모두 발사 or 남은 벽돌이 0이면
    if cnt == N or remains == 0 :
        min_blocks = min(min_blocks, remains)
        return
    
    # 모든 열에 한 줄 씩 떨구자
    for col in range(W):
        # 기존 벽돌들의 상태를 저장
        # 방법 1. 원본을 복사해두고, 다시 되돌리는 방법
        # 1. col 위치에 떨구기 전 상태를 복사(얕은 복사 주의)
        # 2. 원본 리스트의 col 위치에 떨구고
        # 3. cnt + 1 번 재귀 상태로 이동
        # 4. 떨구기 전 상태로 복구

        # 방법 2. 복구 시간이 없는 방식
        # 1. col 위치에 떨구기 전 상태를 복사
        # 2. 복사한 리스트의 col 위치에 떨굼
        # 3. cnt + 1 번 상태로 이동할 때, 복사본을 함께 전달
        copy_arr = [row[:] for row in now_arr]

        row = -1
        # 가장 위 벽돌을 검색
        for r in range(H):
            if copy_arr[r][col] :
                row = r
                break

        if row == -1 : # 벽돌이 없는 열은 pass
            continue

        # 해당 row, col의 숫자부터 시작해서 BFS
        # 행, 열, 숫자를 모두 당아야 함
        q = deque([(row, col, copy_arr[row][col])])
        now_remains = remains -1
        copy_arr[row][col] = 0 # 구슬이 처음 만나는 벽돌 자리 

        #주변 벽돌들을 순차적으로 파괴
        while q:
            r, c, p = q.popleft()
            # 상하좌우의 p칸을 모두 제거
            for k in range(1, p):
                for i in range(4):
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)

                    # 범위 밖이면 pass
                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue
                    
                    # 벽돌이 없으면 pass
                    if copy_arr[nr][nc] == 0:
                        continue

                    q.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc] = 0
                    now_remains -= 1

        # 빈칸 메우기
        # 1번 방법 (swap + idx 포인터)
        # r은 단순히 위 아래로 훑는 스캐너 
        # idx는 다음 벽돌이 놓일 자리를 기억하는 포인터 
        # idx는 0이 나열되어 있어도 아래 빈칸에서 기다리고 있다가
        # 벽돌을 만나면 그 자리로 끌어내려서 swap함 그러고 idx가 올라감

        # 2번 방법(벽돌 모아서 다시 쌓기)
        # stack에 벽돌만 쌓아두고 0으로 초기화 한 후 다시 차례대로 쌓는 방법도 있음
        for c in range(W):
            idx = H - 1
            for r in range(H-1, -1, -1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        shoot(cnt+1, now_remains, copy_arr)


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split() )
    graph = [list(map(int,input().split())) for _ in range(H)]
    min_blocks = float('inf') # 최소 벽돌 수 
    blocks = 0 # 남은 벽돌 수 

    for i in range(H):
        for j in range(W):
            if graph[i][j] : 
                blocks += 1

    shoot(0, blocks, graph)
    print(f"#{tc} {min_blocks}")
