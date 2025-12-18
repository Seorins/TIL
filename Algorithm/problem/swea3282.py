T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) # 물건 개수 / 가방 부피

    # 가방에 넣어서 가치 합 최대화 

    dp = [0] * (K + 1)

    for _ in range(N):
        V, C = map(int, input().split()) # 부피 / 가치 
        
        # 뒤에서부터 채워넣기
        for i in range(K, V-1, -1):
            dp[i] = max(dp[i], dp[i - V] + C)

    print(f"#{tc} {dp[K]}")
