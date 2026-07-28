T = int(input())

for testcase in range(1, T+1):
    s = input()
    stack = []

    for char in s :
        if not stack :
            stack.append(char)        

        elif stack[-1] == char:
            stack.pop()
        
        else : 
            stack.append(char)

    print(f"#{testcase} {len(stack)}")