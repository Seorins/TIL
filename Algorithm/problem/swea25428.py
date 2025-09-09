T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    water = list(map(int, input().split()))

    now = arrive = 0

    