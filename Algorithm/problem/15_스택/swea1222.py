T = 10

def postfix(s):
    stack = []
    string = ''

    for char in s : 
        if char.isdigit():
            string += char
            
        # 우선순위 필요 없음
        else: 
            if stack : 
                string += stack.pop()
        
            stack.append(char)

    while stack:
        string += stack.pop()

    return string    

def calculator(s):
    stack = []

    for char in s :
        if char.isdigit():
            # 계산 해야하니까 숫자로 넣어주기!
            stack.append(int(char))

        else : 
            a = stack.pop()
            b = stack.pop()

            stack.append(a+b)

    return stack.pop()


for tc in range(1, T+1):
    N = int(input())
    s = input()

    string = postfix(s)    
    result = calculator(string)

    print(f"#{tc} {result}")

