T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    stack = [[1]]

    for i in range(1, N):

        row = [1]
        for j in range(1, i):
            row.append(stack[i-1][j-1] + stack[i-1][j])
        row.append(1)
        stack.append(row)


    print(f"#{testcase}")
    for r in stack:
        print(*r)

        
                