T = int(input())

for tc in range(1, T+1):
    N = input()

    binary = ''
    while float(N) > 0 :
        binary += str(int(float(N) * 2))
        N = '0' + str(float(N) * 2)[1:]

        if len(binary) >= 13:
            binary = 'overflow'
            break

    print(f"#{tc} {binary}")