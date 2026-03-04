dir = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def solve(board):
    N = len(board)

    # a+b 큰 것부터
    for total_len in range(2 * (N - 1), 1, -1):
        for a in range(1, N):
            b = total_len - a
            if b < 1 or b >= N:
                continue

            for r in range(N):
                for c in range(N):
                    # 네 꼭짓점이 격자 안에 있는지 먼저 확인
                    if r + a + b >= N:
                        continue
                    if c - b < 0:
                        continue
                    if c + a >= N:
                        continue

                    seen = {board[r][c]}
                    y, x = r, c
                    ok = True

                    # 네 변 따라가기
                    for (dy, dx), length in zip(dir, (a, b, a, b)):
                        for step in range(length):
                            y += dy
                            x += dx

                            # 마지막 칸-> 출발점으로 복귀
                            if (dy, dx) == dir[3] and step == length - 1:
                                if (y, x) != (r, c):
                                    ok = False
                                break

                            if board[y][x] in seen:
                                ok = False
                                break
                            seen.add(board[y][x])

                        if not ok:
                            break

                    if ok:
                        return 2 * total_len

    return -1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{tc} {solve(board)}")