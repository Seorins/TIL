N, M = map(int, input().split())

INF = 1000000000

numbers = [0] * (N+1)

for i in range(1, N+1):
    numbers[i] = int(input())


tree = [0] * (4 * N)

def build(node, start, end):
    if start == end : 
        tree[node] = numbers[start]
        return tree[node]
    mid = (start + end) // 2
    left = build(node * 2, start, mid)
    right = build(node * 2 + 1, mid + 1, end)
    tree[node] = min(left, right)
    return tree[node]


def query(node, start, end, left, right):
    if right < start or end < left : 
        return INF
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    lmin = query(node * 2, start, mid, left, right)
    rmin = query(node * 2 + 1, mid + 1, end, left, right)
    return min(lmin, rmin)

build(1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())
    print(query(1, 1, N, a, b))