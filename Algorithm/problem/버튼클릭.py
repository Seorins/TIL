N, M = map(int, input().split())

buttons = []

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    buttons.append((x1, y1, x2, y2))

SIZE = 1000

# 0번째 행과 열은 경계 처리를 위해 비워둠
prefix = [[0] * (SIZE + 1) for _ in range(SIZE + 1)]

# 클릭 좌표 기록
for _ in range(M):
    x, y = map(int, input().split())
    prefix[x][y] += 1

# 2차원 누적합 생성
for x in range(1, SIZE + 1):
    for y in range(1, SIZE + 1):
        prefix[x][y] += (
            prefix[x - 1][y]
            + prefix[x][y - 1]
            - prefix[x - 1][y - 1]
        )

# 각 버튼이 클릭된 횟수 계산
for x1, y1, x2, y2 in buttons:
    count = (
        prefix[x2][y2]
        - prefix[x1 - 1][y2]
        - prefix[x2][y1 - 1]
        + prefix[x1 - 1][y1 - 1]
    )

    print(count)