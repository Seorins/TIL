
def postfix(s) :
    stack = []
    string = ''
    priority = {'*':2, '+':1}
    
    for char in s:
        if char.isdigit():
            string += char

        else: 
            if stack and priority[char] <= priority[stack[-1]]:
                string += stack.pop()

            stack.append(char)

    while stack:
        string += stack.pop()

    return string

def calculate(s):
    stack = []

    for char in s : 
        if char.isdigit():
            stack.append(int(char))

        else:
            a = stack.pop()
            b = stack.pop()

            if char == '+':
                stack.append(a+b)

            if char == '*':
                stack.append(a*b)

    return stack.pop()


T = 10
for testcase in range(1, T+1):
    N = int(input())
    s = input()

    postfix_result = postfix(s)
    cal_result = calculate(postfix_result)

    print(f"#{testcase} {cal_result}")

