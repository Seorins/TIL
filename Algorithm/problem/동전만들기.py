n = int(input())

coins = [1, 3, 4]

# 처음에는 아직 만들 수 없다고 가정
dp = [float('inf')] * (n + 1)

# 0원을 만드는 데 필요한 동전은 0개
dp[0] = 0

for i in range(1, n + 1):
    for coin in coins:
        # 현재 금액보다 동전이 작거나 같을 때만 사용 가능
        if i >= coin:
            dp[i] = min(
                dp[i],
                dp[i - coin] + 1
            )

print(dp[n])