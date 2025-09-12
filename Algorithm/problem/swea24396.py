T = int(input())

for testcase in range(1, T+1):
    B, W, X, Y, Z = map(int, input().split())

    max_num = -(float('inf'))
    for c in range(min(B, W) + 1):
        black = B - c
        white = W - c
        mix = (c * Z) * 2 

        max_num = max(max_num, black + white + mix)

    print(max_num)