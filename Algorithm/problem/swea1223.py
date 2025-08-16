T = 10

# 후위 표기식 변환
def postfix(s) :
    stack = []
    priority = {'+':1, '*':2}
    string = ''
    
    for char in s:
        # 숫자면 바로 추가
        if char.isdigit():
            string += char
        
        # 우선순위 따져서 추가하기 (stack에 대기 시킴)
        else : 
            while stack and priority[char] <= priority[stack[-1]] :
                string += stack.pop() 

            stack.append(char)

    # 남은 거 추가하기
    while stack:
        string += stack.pop()

    return string

# 값 계산
def calculate(s):
    stack = []

    for char in s:
        # 숫자면 바로 추가
        if char.isdigit():
            stack.append(int(char))

        else: 
            # 스택에 추가한 거 꺼내와서 연산하기 -> 계산된 값 넣기
            a = stack.pop()
            b = stack.pop()

            if char == '*':
                stack.append(a*b)
            elif char =='+':
                stack.append(a+b)

    # 마지막에 남은 건 최종 값
    return stack.pop()

for testcase in range(1, T+1):
    N = int(input())
    s = input()

    postfix_result = postfix(s)
    cal_result = calculate(postfix_result)

    print(f"#{testcase} {cal_result}")

