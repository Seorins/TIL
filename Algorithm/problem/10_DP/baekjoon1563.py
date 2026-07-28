N = int(input())
MOD = 1_000_000

# dp[i][l][a]
dp = [[[0] * 3 for _ in range(2)] for _ in range(N + 1)]
dp[0][0][0] = 1

for i in range(N):
    for l in range(2):
        for a in range(3):
            v = dp[i][l][a]
            if v == 0:
                continue

            # 1) O (출석)
            dp[i + 1][l][0] = (dp[i + 1][l][0] + v) % MOD

            # 2) A (결석) - 연속결석 3이면 안 됨
            if a < 2:
                dp[i + 1][l][a + 1] = (dp[i + 1][l][a + 1] + v) % MOD

            # 3) L (지각) - 지각 2번이면 안 됨
            if l < 1:
                dp[i + 1][l + 1][0] = (dp[i + 1][l + 1][0] + v) % MOD

ans = 0
for l in range(2):
    for a in range(3):
        ans = (ans + dp[N][l][a]) % MOD

print(ans)
