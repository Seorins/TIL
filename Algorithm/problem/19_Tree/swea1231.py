def inorder(node):
    if node == 0:
        return 
    
    if len(words[node]) > 1:
        inorder(int(words[node][1]))

    print(words[node][0], end = "")

    if len(words[node]) > 2:
        inorder(int(words[node][2]))

for tc in range(1, 11):
    N = int(input())
    words = {i:[] for i in range(1, N+1)}
    user = [list(input().split()) for _ in range(N)]

    for x in user:
        words[int(x[0])] = x[1:]

    print(f"#{tc}", end= " ")
    inorder(1)
    print()
    