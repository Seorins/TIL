import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
R -= 1

tree = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    tree[u].append(v)
    tree[v].append(u)

visited = [False] * N
subtree = [0] * N

def dfs(u):
    visited[u] = True
    subtree[u] = 1

    for v in tree[u]:
        if not visited[v]:
            dfs(v)
            subtree[u] += subtree[v]

dfs(R)

for _ in range(Q):
    u = int(input())
    u -= 1
    print(subtree[u])