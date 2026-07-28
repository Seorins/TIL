T = int(input())

for tc in range(1, T+1):
    day, month, t_month, year = map(int, input().split())
    days = [0] + list(map(int, input().split()))

    dp = [0] * 13

    dp[1] = min(days[1] * day, month)
    dp[2] = dp[1] + min(days[2] * day, month)

    for m in range(3, 13):
        dp[m] = min(dp[m-3] + t_month
                        , dp[m-1] + (days[m] * day)
                        , dp[m-1] + month)

    ans = min(dp[12], year)

    print(f"#{tc} {ans}")