from collections import deque

def bfs(start_node):
    # q의 의미 : 다음에 방문해야 할 노드들(후보열, 대기열)
    dq = deque([start_node])

    while dq : 
        #1. 가장 앞의 노드를 뽑는다
        # 2. 해당 노드에서 갈 수 있는 노드들을 queue에 넣는다
        now = dq.popleft()

        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = 1
                dq.append(next)


V, E = map(int, input())

# 인접 리스트 (연결된 간선만 저장) 
graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0] * (V+1)
visited[1] = 1
bfs(1)