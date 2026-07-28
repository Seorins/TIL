def calc(i):
    if len(node[i]) == 1:
        return int(node[i][0])
    
    else:
        operator, left, right = node[i]
        left_v = calc(int(left))
        right_v = calc(int(right))
 
        if operator == '+':
            return left_v + right_v
        
        elif operator == '-':
            return left_v - right_v
        
        elif operator == '*':
            return left_v * right_v
        
        elif operator == '/':
            return left_v / right_v
 
 
for tc in range(1, 11):
    N = int(input())
    node = [0] * (N + 1)

    for _ in range(N):
        node_info = list(input().split())

        node_num = int(node_info[0])

        if node_info[1] not in '-+*/':
            node[node_num] = [node_info[1]]

        else:
            node[node_num] = node_info[1:]

    result = int(calc(1))

    print(f'#{tc} {result}')