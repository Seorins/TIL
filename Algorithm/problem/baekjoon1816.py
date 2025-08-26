T = int(input())

for testcase in range(1, T+1):
    number = int(input())

    for i in range(2, 1000001):
        if number % i == 0:
            print("NO")
            break

        if number == 1000000:
            print("YES")
            
    