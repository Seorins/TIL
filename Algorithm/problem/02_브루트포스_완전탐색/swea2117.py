'''
N x N 도시
각 칸은 집(1), 빈칸(0)

서비스 영역: 마름모 형태 / 범위 k
운영 비용: k^2 + (k-1)^2

집 하나당 수익 m / 집 개수 × m

(집 개수 × m) - (운영 비용) >= 0

손해 없이 서비스 가능한 집의 최대 개수 구하기
'''

def check(r, c):
    global result
    
    # 거리별 집 개수 저장
    dist_cnt = [0] * max_d

    for hr, hc in houses:
        d = abs(r - hr) + abs(c - hc)
        dist_cnt[d + 1] += 1

    # 현재 범위 안 집 개수
    total = 0

    for k in range(max_d):
        if dist_cnt[k]:
            total += dist_cnt[k]

             # 운영 비용
            cost = k*k + (k-1)*(k-1)

            # 손해가 아니면 최대값 갱신
            if total * m - cost >= 0:
                result = max(result, total)


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    houses = set()
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                houses.add((i, j))

    max_d = 2 * n # 최대 거리 범위
    result = 0  # 최대 서비스 가능 집 수

    for i in range(n):
        for j in range(n):
            check(i, j)

    print(f"#{tc} {result}")