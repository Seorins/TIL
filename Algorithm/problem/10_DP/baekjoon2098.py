import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

INF = 16000000
dp = [[0] * (1 << N) for _ in range(N)]

def dfs(cur, visited):
    # 모든 도시 방문
    if visited == (1 << N) - 1:
        return INF if graph[cur][0] == 0 else graph[cur][0]

    # 이미 계산된 경우
    if dp[cur][visited] != 0:
        return dp[cur][visited]

    min_cost = INF

    for i in range(N):
        # 갈 수 없거나 이미 방문한 경우 skip
        if graph[cur][i] == 0 or (visited & (1 << i)):
            continue
        
        cost = graph[cur][i] + dfs(i, visited | (1 << i))
        min_cost = min(min_cost, cost)

    dp[cur][visited] = min_cost
    return min_cost

print(dfs(0, 1))