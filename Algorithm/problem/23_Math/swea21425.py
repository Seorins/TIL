T = int(input())
result = []

# x = A , y = B N = 초과될 값
for i in range(T):
    A, B, N = map(int, input().split())
    cnt = 0
    x = 0
    y = 0
    x_num = max(A, B)
    y_num = min(A, B)

    while True:
        y_num += x_num

        x = max(x_num, y_num)
        y = min(x_num, y_num)

        x_num = x
        y_num = y

        if y_num > N:
            break

        cnt += 1

    result.append(cnt)

for r in result:
    print(r)
