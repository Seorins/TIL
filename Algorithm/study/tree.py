class Node: 
    def __init__(self, value):
        self.value = value
        self.children = []

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")
J = Node("J")
K = Node("K")

# children 리스트 안에는 "객체 B, 객체 C, 객체 D"에 대한 주소값이 들어 있어서
# 그걸 통해 해당 노드로 이동할 수 있게 됨
A.children = [B, C, D]
B.children = [E, F]
F.children = [K]
C.children = [G]
D.children = [H, I, J]

root = A

class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

A = BinaryNode("A")
B = BinaryNode("B")
C = BinaryNode("C")
D = BinaryNode("D")
E = BinaryNode("E")

A.left, A.right = B, C
B.left, B.right = D, E

def preorder(node):
    if node :
        print(node.value, end = " ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node : 
        inorder(node.left)
        print(node.value, end = " ")
        inorder(node.right)

def postorder(node):
    if node : 
        postorder(node.left)
        postorder(node.right)
        print(node.value, end= " ")

print("Preorder: ", end= " ")
preorder(A)
print("\nInorder: ", end= " ")
preorder(A)
print("Preorder: ", end= " ")
preorder(A)



# 특정 노드 찾는 방법
# 이진 탐색 트리(BST)에서 탐색
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_bst(root, target):
    # 루트가 없으면 못 찾음
    if root is None:
        return None
    
    # 값이 일치하면 찾음
    if root.value == target:
        return root
    
    # target이 더 작으면 왼쪽에서 탐색
    if target < root.value:
        return search_bst(root.left, target)
    
    # target이 더 크면 오른쪽에서 탐색
    return search_bst(root.right, target)


# 예시
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

found = search_bst(root, 40)
print(found.value if found else "없음")  # 40



# 일반 트리에서 찾기
# DFS 탐색(재귀)
def search_tree(root, target):
    if root is None:
        return None
    if root.value == target:
        return root
    
    # 왼쪽에서 먼저 찾기
    left_result = search_tree(root.left, target)
    if left_result:
        return left_result
    
    # 오른쪽에서 찾기
    return search_tree(root.right, target)


# BFS 탐색(큐)
from collections import deque

def search_tree_bfs(root, target):
    q = deque([root])
    while q:
        node = q.popleft()
        if node.value == target:
            return node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return None
