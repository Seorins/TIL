def solution(tickets):
    graph = {}

    for a, b in tickets:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)

    for airport in graph:
        graph[airport].sort(reverse=True)

    result = []

    def dfs(cur):
        while cur in graph and graph[cur]:
            nxt = graph[cur].pop()
            dfs(nxt)

        result.append(cur)

    dfs("ICN")

    return result[::-1]