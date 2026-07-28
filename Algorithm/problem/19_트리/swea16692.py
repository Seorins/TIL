def inorder(node, N):
    global num 
    if node <= N:
        inorder(node*2, N)
        tree[node] = num
        num += 1
        inorder(node*2+1, N)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1

    inorder(1, N)

    print(f"#{tc} {tree[1]} {tree[N//2]}")


