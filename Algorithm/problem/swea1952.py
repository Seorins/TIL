import sys
sys. stdin = open("input.txt", 'r')

'''
1일 이용권  / 1달 이용권 / 3달 이용권 / 1년 이용권

이용권의 요금과 각 달의 이용 계획이 주어질 때
가장 적은 비용 내기
'''
def dfs(idx, price):
    global min_price

    # 가지치기
    if price >= min_price:
        return 

    if idx > 12:
        min_price = min(min_price, price)
        return 

    dfs(idx+1, price + (plan[idx]*day))
    dfs(idx+1, price + month)
    dfs(idx+3, price + t_month)
    dfs(idx+12, price + year)

T = int(input())

for tc in range(1, T+1):
    day, month, t_month, year = map(int, input().split())
    plan = list(map(int, input().split()))

    min_price = float('inf')

    dfs(0, 0)

    print(f"#{tc} {min_price}")