T = int(input())

def is_paired(s):
    stack = []
    pairs = {']':'[', '}':'{', ')':'('}

    for char in s :
        if char in '[{(':
            stack.append(char)

        elif char in ']})':
            if not stack:
                return 0
            top = stack.pop()

            if pairs[char] != top:
                return 0

    if not stack : 
        return 1

    else:
        return 0

for testcase in range(1, T+1):
    s = input()

    result = is_paired(s)
    print(f"#{testcase} {result}")