stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print('---------------------------------------------')

#top = - 1로 하는 이유 => 빈 스택을 표현
top = -1
stack = [0] * 10

top += 1
stack[top] = 1


# 이렇게 괄호 종류를 한 번에 확인할 수 있음
# for x in arr:
    # if x in ['[', '{', '(' ]: