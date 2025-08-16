def dfs(graph, start, end, visited):
    
    if start == end : 
        return True

    visited.add(start)

    for node in graph[start]:
        if node not in visited:
            if dfs(graph, node, end, visited):
                return True

    return False


T = 10

for tc in range(1, T+1):
    testcase, num = map(int, input().split())
    graph = {i:[] for i in range(100)}
    row = list(map(int, input().split()))

    for i in range(0, len(row), 2):
        x, y = row[i], row[i+1]
        graph[x].append(y)

    visited = set()

    start = 0  
    end = 99

    result = 0
    if dfs(graph, start, end, visited):
        result = 1

    print(f"#{testcase} {result}")
