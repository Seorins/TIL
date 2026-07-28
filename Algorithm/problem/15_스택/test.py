T = int(input())
 
def calculate(s) :
    stack = []
     
    for char in s : 
        if char.isdigit():
            stack.append(int(char))
 
        elif char == '.':
            if len(stack) != 1:
                return 'error'
            return stack.pop()
 
        else:
            if len(stack) < 2:
                return 'error'    
            a = int(stack.pop())
            b = int(stack.pop())
 
            if char == '*':
                stack.append(a*b)
             
            elif char == '+':
                stack.append(a+b)
 
            elif char == '-':
                stack.append(b-a)
 
            elif char == '/':     
                if a == 0:
                    return 'error'  
                stack.append(b//a)
 
            else: 
                return 'error'
    return 'error'
 
 
for testcase in range(1, T+1):
    s = input().split()
    result = calculate(s)    
 
    print(f"#{testcase} {result}")