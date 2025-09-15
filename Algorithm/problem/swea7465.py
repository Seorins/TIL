from collections import deque

def bfs(S, visited):
    dq = deque()
    dq.append(S)
    visited[S] = True
    
    while dq: 
        v = dq.popleft()

        for next in people[v]:
            if not visited[next] :
                visited[next] = True
                dq.append(next)

    return visited

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    people = {i:[] for i in range(1, N+1)}

    # 서로를 알고 있으므로 양방향 
    for _ in range(M):
        x, y = map(int, input().split())
        people[x].append(y)
        people[y].append(x)

    visited = [False] * (N+1)
    cnt = 0

    for i in range(1, N+1):
        if not visited[i]:
            bfs(i, visited)
            cnt += 1

    print(f"#{tc} {cnt}")