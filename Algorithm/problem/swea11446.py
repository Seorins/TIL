T = int(input())

for tc in range(1, T+1):
    # N = 사탕 종류의 개수
    # M = 사탕 가방 안에 정확히 M개의 사탕이 들어있어야 함
    N, M = map(int, input().split())
    candy = list(map(int, input().split()))

    # 가방을 몇 개 써야 M개의 똑같은 비율의 사탕 개수가 들어갈 수 있나
    # 반드시 모든 종류의 사탕을 쓸 필요는 없음 (안에 구성만 같으면 됨)
    left = 1
    # 가장 많은 사탕 종류 기준
    # 그 사탕을 가방에 1개씩만 넣으면 이게 최대 
    right = max(candy)

    while left <= right : 
        # 가방 개수 = mid 
        mid = (left + right) // 2

        # 가방 개수가 mid개라고 할 때
        # 가방 안에 문제의 조건을 맞춰서 사탕 개수를 몇 개 넣을 수 있는가
        count = 0
        # i번 사탕
        for i in range(N):
            # i번 사탕을 가방의 개수만큼 나눠야 
            # 모든 가방 안에 있는 사탕 비율이 같다
            count += candy[i] // mid

        # count가 답이 되는지 안되는지 ? 
        # 문제에서 원하는 것은 count가 정확히 M
        if count < M : 
            # 세어봤는데 문제에서 원하는 M개보다 작음
            # 사탕 가방의 개수 줄여야 함 
            # 답이 될 가능성 xx
            right = mid - 1

        else :
            # 세어봤는데 문제에서 원하는 M개보다 많음
            # 사탕가방의 개수 늘려볼 수 있음
            # 최소 답은 right로 확정
            left = mid + 1

    print(f"#{tc} {right}")