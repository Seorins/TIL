from collections import deque

def bfs(S):
    visited = [False]*101
    dq = deque()
    dq.append(S)
    visited[S] = True

    last_level = []

    while dq:
        size = len(dq)
        node_level = []

        for _ in range(size):
            v = dq.popleft()
            node_level.append(v)

            for next in users[v]:
                if not visited[next] :
                    dq.append(next)
                    visited[next] = True

        last_level = node_level 

    return max(last_level)

for tc in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    users = {i:[] for i in range(1, 101)}

    for i in range(0, N, 2):
        users[arr[i]].append(arr[i+1])

    print(f"#{tc} {bfs(S)}")

