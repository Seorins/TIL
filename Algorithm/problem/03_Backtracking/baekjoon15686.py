def dfs(idx, now):
    global result
    
    if len(now) == M:
        total = 0
        for hx, hy in house:
            dist = 10 ** 9
            for cx, cy in now:
                dist = min(dist, abs(hx-cx) + abs(hy-cy))

            total += dist
        result = min(result, total)
        return 
    
    for i in range(idx, len(chicken)):
        dfs(i+1, now + [chicken[i]])

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))

        elif city[i][j] == 2:
            chicken.append((i, j))

result = 10**9
dfs(0, [])
print(result)