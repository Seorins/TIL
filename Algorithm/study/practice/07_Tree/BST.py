# -------------------------------
# 이진 탐색 트리 (Binary Search Tree) 구현 예시
# -------------------------------

# 노드 정의 (연결 리스트 구조)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None    # 왼쪽 자식
        self.right = None   # 오른쪽 자식

# 삽입 연산
def insert(root, key):
    # 1) 현재 루트가 비어있으면 새로운 노드 생성
    if root is None:
        return Node(key)

    # 같으면 반환
    if root.value == key:
        return True
    
    # 2) 삽입할 값이 루트보다 작으면 왼쪽 서브트리에 삽입
    if key < root.value:
        root.left = insert(root.left, key)

    # 3) 삽입할 값이 루트보다 크거나 같으면 오른쪽 서브트리에 삽입
    else:
        root.right = insert(root.right, key)

    return root  # 갱신된 루트 반환

# 중위 순회 (왼쪽 → 부모 → 오른쪽)
def inorder(node):
    if node:
        inorder(node.left)              # 왼쪽 서브트리 방문
        print(node.value, end=" ")      # 부모(자기 자신) 출력
        inorder(node.right)             # 오른쪽 서브트리 방문

# -------------------------------
# 사용 예시
# -------------------------------
root = None
for num in [5, 3, 7, 2, 4, 6, 8]:  # 차례대로 삽입
    root = insert(root, num)

inorder(root)  # 출력: 2 3 4 5 6 7 8 (오름차순 정렬됨)


