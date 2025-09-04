class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

A.left = D
A.right = E
E.left = B
E.right = C

def preorder(t):
    if t:
        print(t.value, end = " ")
        preorder(t.left)
        preorder(t.right)

preorder(A)
print()

def inorder(t):
    if t:
        inorder(t.left)
        print(t.value, end = " ")
        inorder(t.right)
inorder(A)
print()

def postorder(t):
    if t:
        postorder(t.left)
        postorder(t.right)
        print(t.value, end=" ")
postorder(A)
print()