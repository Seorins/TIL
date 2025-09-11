def dfs(idx, price):
    global min_price

    if price >= min_price : 
        return  

    if idx >= 12 :
        min_price = min(min_price, price)
        return

    dfs(idx + 1, price + day*plan[idx])
    dfs(idx + 1, price + month)
    dfs(idx + 3, price + three_m)
    dfs(idx + 12, price + year)

T = int(input())

for tc in range(1, T+1):
    day, month, three_m, year = map(int, input().split())
    plan = list(map(int, input().split()))
    min_price = float('inf')

    dfs(0, 0)

    print(f"#{tc} {min_price}")