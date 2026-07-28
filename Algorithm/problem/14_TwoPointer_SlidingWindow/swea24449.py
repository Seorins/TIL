T = int(input())

for tc in range(1, T+1):
    N, K = map(int(input().split())) # 야구 선수 수, 허용 실력 차
    players = list(map(int(input()))) # 선수 실력
    players.sort()
    max_team = 0

    # 투포인터 활용
    # 오른쪽으로 가다가 허용 범위 넘으면 왼쪽 줄이기 

    left = 0

    for i in range(N) :
        while players[i] - players[left] > K:
            left += 1

        max_team = max(max_team, i - left + 1)

    print(f"#{tc} {max_team}")




    