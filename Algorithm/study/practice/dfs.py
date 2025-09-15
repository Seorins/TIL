def dfs(node):
    print(node, end=' ')
    # 다음 재귀 호출
    # node로부터 갈 수 있는 노드들을 모두 확인
    # --> 그 중에서 한 곳으로 진행
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node)


V, E = map(int, input())

# 인접 리스트 (연결된 간선만 저장) 
graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0] * (V+1)
visited[1] = 1
dfs(1)