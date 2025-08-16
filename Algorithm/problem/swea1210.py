T = 10

for testcase in range(1, T + 1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 마지막 줄 순회하고 2인 곳 찾기
    # 2에서부터 위, 오른쪽 왼쪽으로 가기 (아래 필요 x)

    # 왼쪽 위 오른쪽
    di = [0, -1, 0]
    dj = [-1, 0, 1]

    dir = 1  # 기본 위쪽

    # 도착지점 찾기
    # 행은 마지막 고정 열 순회
    for i in range(99, 98, -1):  # 마지막 줄
        for j in range(100):
            if ladder[i][j] == 2:
                fin_i = i
                fin_j = j
                break

    # 이제 올라가면서 방향 전환 해주기
    # i가 0이 되면 첫 번째 줄
    while fin_i > 0:

        # 길 가다가 오른쪽 길 있을 경우 (열 +1)
        if fin_j + 1 < 100 and ladder[fin_i][fin_j + 1] == 1:
            dir = 2
            while (
                fin_j + 1 < 100 and ladder[fin_i][fin_j + 1] == 1
            ):  # 오른쪽 길이 1일 동안 계속 이동
                fin_j += 1
            fin_i -= 1

        # 길 가다 왼쪽 길 있을 경우 (열 -1)
        elif fin_j - 1 >= 0 and ladder[fin_i][fin_j - 1] == 1:
            dir = 0
            while fin_j - 1 >= 0 and ladder[fin_i][fin_j - 1] == 1:  # 오른쪽 길이 1일 동안 계속 이동
                fin_j -= 1
            fin_i -= 1

        # 위로 이동
        else:
            fin_i -= 1

    print(f"#{testcase} {fin_j}")
