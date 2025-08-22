def dfs(N, subtree):
    subtree.append(N)
    
    for next in tree[N]:
        dfs(next, subtree)
        
T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]
    subtree = []
    
    for i in range(0, len(arr), 2):
        tree[arr[i]].append(arr[i+1])
    
    dfs(N, subtree)

    print(f"#{tc} {len(subtree)}")
