S = input()

res = []
stack = []
in_tag = False

for ch in S:
    if ch == '<':
        while stack:
            res.append(stack.pop())
        in_tag = True
        res.append(ch)

    elif ch == '>':
        in_tag = False
        res.append(ch)

    elif in_tag:
        res.append(ch)

    else:
        if ch == ' ':
            while stack:
                res.append(stack.pop())
            res.append(' ')
        else:
            stack.append(ch)

while stack:
    res.append(stack.pop())

print(''.join(res))


