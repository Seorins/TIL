'''
보호 필름 : 두께 D, 가로 크기 W
세로 방향으로 동일한 특성 셀들이 k개 이상 있어야 성능검사 통과
특정 막에 약품을 넣으면 해당 특성으로 다 바뀜 (A/B)
약품의 최소 투입 횟수 / 그냥 통과는 0

열 단위로 검사하고 행 단위로 바꾸고.. 
'''

def check():
    global D, W, K, film

    if K == 1:
        return True

    for c in range(W):
        cnt = 1
        passed = False

        for r in range(D-1):
            if film[r][c] == film[r+1][c]:
                cnt += 1
            else:
                cnt = 1

            if cnt >= K:
                passed = True
                break

        if not passed:
            return False

    return True


def dfs(row, cnt):
    global D, W, K, film, result

    if cnt >= result:
        return

    if row == D:
        if check():
            result = min(result, cnt)
        return

    # 투입 안 함
    dfs(row + 1, cnt)

    temp = film[row][:] 

    # A 투입
    film[row] = [0] * W
    dfs(row + 1, cnt + 1)

    # B 투입
    film[row] = [1] * W
    dfs(row + 1, cnt + 1)

    film[row] = temp  # 복구


T = int(input())

for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    result = D # 어차피 최대 깊이 이상으로 못 감

    dfs(0, 0)

    print(f"#{tc} {result}")

