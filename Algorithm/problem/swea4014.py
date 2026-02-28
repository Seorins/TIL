'''
N x N 지도
경사로 길이 X

1. 인접한 칸의 높이 차이가 2 이상이면 불가능
2. 높이가 1 낮아지거나 높아질 경우 길이 X만큼 같은 높이의 칸이 필요
3. 경사로는 겹쳐서 설치할 수 없음 (visited로 체크)
'''

def check(board, n, x):
    visited = [False] * n # 경사로 설치 여부 체크
     
    # 높이 차이가 2 이상이면 바로 불가능
    for i in range(n-1):
        if abs(board[i] - board[i+1]) >= 2:
            return False
     
        # 오르막길 
        if board[i] < board[i+1]:
            for j in range(x):
                if i-j<0 or board[i-j] != board[i] or visited[i-j]:
                    return False
                visited[i-j] = True

        # 내리막길
        elif board[i] > board[i+1]:
            for j in range(x):
                if i +1+j >=n or board[i+1+j] != board[i+1] or visited[i+1+j]:
                    return False
                visited[i+1+j] = True

    return True
 
T = int(input())

for tc in range(1, T+1):
    N, X = map(int,input().split()) # 한 변의 크기, 경사로의 길이
    board = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    
    # 가로
    for i in range(N):
        if check(board[i], N, X):
            cnt += 1
     
    # 세로
    for j in range(N):
        col_lst = [board[i][j] for i in range(N)]
        if check(col_lst, N, X):
            cnt += 1
 
    print(f'#{tc} {cnt}')