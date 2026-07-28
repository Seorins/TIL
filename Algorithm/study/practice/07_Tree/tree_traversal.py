arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

# 일차원 배열로 저장하는 방식
# 개인 과제



# 그래프로 저장하는 방식 
nodes = [[] for _ in range(14)]

for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].append(child_node)

    # 자식이 없는 걸 표현하기 위해 None을 삽입
    # 자식이 하나만 없으면 None하나 삽입
    # 둘다 없으면 None 둘다 삽입 (양쪽)
    for li in nodes:
        for _ in range(len(li), 2):
            li.append(None)


    def order(node):
        if node == None:
            return
        
        # nodes[node] : node에 연결된 번호들(자식 번호들)
        # nodes[node][0] : 첫 번쨰 자식 번호
        # nodes[node][1] :  두 번째 자식 번호
        print(node, end = ' ') # 전위 순회
        order(nodes[node][0])
        order(nodes[node][1])


    order(1)