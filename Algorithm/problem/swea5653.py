'''
비활성 life시간 -> 활성
활성된 첫 1시간에 번식(=활성 시작 순간 번식 처리)
활성 life시간 지나면 죽음(죽어도 칸은 점유)
동시에 번식하면 생명력 큰 놈 우선
K시간 후 살아있는 세포 수(비활성+활성)
'''

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # 세로, 가로, 시간
    board = [list(map(int, input().split())) for _ in range(N)]

    row, col = N + 2*K + 2, M + 2*K + 2
    offset = K + 1
    cell_map = [[0] * col for _ in range(row)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    cells = []
    for i in range(N):
        for j in range(M):
            x = board[i][j]
            if x:
                r, c = i + offset, j + offset
                cell_map[r][c] = x
                cells.append([r, c, x, x, 1]) 

    for _ in range(K):
        new_cells = {}  # 이번 시간 번식 후보
        nxt = [] # 다음 상태 세포들

        for r, c, life, timer, status in cells:
            timer -= 1

            # 비활성 끝 -> 활성 시작
            if status == 2 and timer == life - 1:
                for a, b in zip(di, dj):
                    ni, nj = r + a, c + b
                    if cell_map[ni][nj] == 0:
                        prev = new_cells.get((ni, nj), 0)
                        if prev < life:
                            new_cells[(ni, nj)] = life

             
            if timer == 0:
                if status == 1: # 비활성 끝 -> 활성 시작
                    status = 2
                    timer = life
                else: # 활성 끝 -> 죽음
                    status = 0

            if status != 0:
                nxt.append([r, c, life, timer, status])

        for (nr, nc), n_life in new_cells.items():
            cell_map[nr][nc] = n_life
            nxt.append([nr, nc, n_life, n_life, 1])

        cells = nxt

    print(f"#{tc} {len(cells)}")