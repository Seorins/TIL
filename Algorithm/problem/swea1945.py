T = int(input())

for testcase in range(1, T + 1):
    number = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while number != 1:

        if number % 2 == 0:
            a += 1
            number = number // 2

        elif number % 3 == 0:
            b += 1
            number = number // 3

        elif number % 5 == 0:
            c += 1
            number = number // 5

        elif number % 7 == 0:
            d += 1
            number = number // 7

        elif number % 11 == 0:
            e += 1
            number = number // 11

        else:
            break

    print(f"#{testcase} {a} {b} {c} {d} {e}")
