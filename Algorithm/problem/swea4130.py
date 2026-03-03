# 특이한 자석

def dfs(idx, dir):
    # 오른쪽 전파
    if idx < 3:
        # 2번 톱니 vs 오른쪽 6번 톱니 비교
        if magnet[idx][2] != magnet[idx + 1][6] and not v[idx + 1]:
            v[idx + 1] = 1
            dfs(idx + 1, -dir) # 반대 방향

    # 왼쪽 전파
    if idx > 0:
        # 2번 톱니 vs 오른쪽 6번 톱니 비교
        if magnet[idx][6] != magnet[idx - 1][2] and not v[idx - 1]:
            v[idx - 1] = 1
            dfs(idx - 1, -dir) # 반대 방향

    # 회전 
    if dir == 1: # 시계
        magnet[idx] = [magnet[idx][-1]] + magnet[idx][:-1]
    else: # 반시계
        magnet[idx] = magnet[idx][1:] + [magnet[idx][0]]


T = int(input())

for tc in range(1, T + 1):
    K = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        idx, dir = map(int, input().split())
        idx -= 1

        v = [0] * 4
        v[idx] = 1
        dfs(idx, dir)

    result = 0
    for i in range(4):
        if magnet[i][0] == 1:
            result += 2 ** i

    print(f"#{tc} {result}")