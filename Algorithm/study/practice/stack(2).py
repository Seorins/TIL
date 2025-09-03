def check_parentheses(s):
    stack = []
    for ch in  s :
        if ch == '(':
            stack.append(ch)

        elif ch == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

print(check_parentheses("()"))       
print(check_parentheses("(()())"))   
print(check_parentheses("(()"))     
print(check_parentheses(")("))  



def is_balanced(s):
    stack = []
    pairs = {')' : '(', '}' : '{', ']' : '['}

    for ch in s :
        if ch in '({[': # 왼쪽처리
            stack.append(ch)
        
        elif ch in ']})':
            if not stack: 
                return False
            top = stack.pop()
        
            if pairs[ch] != top:
                return False
    
    return not stack

print(is_balanced("()[]{}"))   
print(is_balanced("({[]})"))   
print(is_balanced("({)}"))     
print(is_balanced("(()"))     
print(is_balanced(")("))