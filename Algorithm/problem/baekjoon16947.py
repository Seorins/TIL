'''
1개의 순환역 2개의 지선

1. 순환역 찾기 
-> 시작역에서 시작해서 시작역으로 다시 돌아와야함 
start == idx 

* 하나의 역만 갔다가 다시 돌아오는 건 x
1 - 2 - 1
cnt 관리 

- dfs 활용

2. 역과 순환선 사이의 최소 거리 구하기
- bfs 활용 
'''

from collections import deque
import sys
sys.setrecursionlimit(100000)


def dfs(start, now, cnt):
    global is_cycle
    for nxt in graph[now]:
        if nxt == start and cnt >= 2:
            cycle[now] = True
            is_cycle = True
            return True

        if not visited[nxt]:
            visited[nxt] = True
            if dfs(start, nxt, cnt + 1):
                cycle[now] = True
                return True
            visited[nxt] = False
    return False


def bfs():
    q = deque()
    dist = [-1] * (n + 1)

    for i in range(1, n + 1):
        if cycle[i]:
            q.append(i)
            dist[i] = 0

    while q:
        x = q.popleft()
        for nxt in graph[x]:
            if dist[nxt] == -1:
                dist[nxt] = dist[x] + 1
                q.append(nxt)

    return dist


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
cycle = [False] * (n + 1)
is_cycle = False

for i in range(1, n + 1):
    if not is_cycle:
        visited[i] = True
        dfs(i, i, 0)
        visited[i] = False

dist = bfs()
print(*dist[1:])
