T = 10 

for testcase in range(1, T+1):
    num, s = input().split()

    stack = []

    for char in s:

        if not stack : 
            stack.append(char)    

        else : 
            if stack[-1] == char : 
                stack.pop()

            else:
                stack.append(char)
 

    print(f"#{testcase} {''.join(stack)}")
