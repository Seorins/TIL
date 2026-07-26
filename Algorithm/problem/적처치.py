def solution(energy_power): 
    n = len(energy_power)

    # 양수 -> 작은 값부터 
    # 음수는 양수 뒤에 배치 
    positives = sorted(x for x in energy_power if x >= 0) 
    negatives = sorted(x for x in energy_power if x < 0)

    order = positives + negatives

    # k명을 처치하기 위한 최소 시작 체력
    dp = [float('INF')] * (n+1)

    dp[0] = 1

    cnt = 0

    # 현재 적을 기존 전투 순서의 앞에 붙이므로 뒤쪽부터 확인
    for x in reversed(order):
        cnt += 1
        # 같은 적을 두 번 사용하는 것을 막기 위해 뒤에서부터 갱신
        for k in range(cnt, 0, -1):
            required = max(
                x+1, # 현재 적과 싸우기 위한 체력
                dp[k-1]-x # 현재 적을 잡은 뒤 나머지를 잡기 위한 체력
            )

            dp[k] = min(dp[k], required)

    return dp[1:]

