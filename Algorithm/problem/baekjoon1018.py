'''
M*N 크기 보드
보드를 잘라서 8*8 체스판 제작
흰색 검은색 번갈아서 칠해져 있어야 함

경우 2가지 뿐 -> 맨 왼쪽 위 칸 흰색 / 검은색
-> 두 가지 경우 중 적은 거 선택해야 함

보드가 체스판처럼 칠해져 있다는 보장이 없음 -> 자른 후 몇 개 정사각형 다시 색칠 
칠해야 하는 정사각형의 최소 개수 
'''

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
min_cnt = float('inf')

# 8*8 보드를 만든 후 돌기
for i in range(N-7):
    for j in range(M-7):
        # 두 가지 경우 다 확인해봐야 함
        cnt_w = 0  # W로 시작
        cnt_b = 0  # B로 시작
        
        for p in range(8):
            for q in range(8):
                if (p + q) % 2 == 0:
                    if board[i+p][j+q] != 'W':
                        cnt_w += 1
                    if board[i+p][j+q] != 'B':
                        cnt_b += 1
                        
                else:
                    if board[i+p][j+q] != 'B':
                        cnt_w += 1
                    if board[i+p][j+q] != 'W':
                        cnt_b += 1
                        
        min_cnt = min(min_cnt, cnt_w, cnt_b)

print(min_cnt)