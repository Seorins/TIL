def dfs(idx, total):
    global cnt

    if idx == N :
        if total == K : 
            cnt += 1
        return 

    # 선택 하고
    dfs(idx+1, total+number[idx])

    # 선택 안 하고
    dfs(idx+1, total)


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    number = list(map(int, input().split()))
    cnt = 0

    dfs(0, 0)

    print(f"#{tc} {cnt}")