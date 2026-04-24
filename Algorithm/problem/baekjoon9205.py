from collections import deque

def bfs(places):
    visited = [False] * len(places)
    q = deque([0]) 
    visited[0] = True

    while q:
        cur = q.popleft()
        x, y = places[cur]
    
        nx, ny = places[-1]

        if abs(x - nx) + abs(y - ny) <= 1000:
            return "happy"

        for i in range(n):
            if not visited[i]:
                nx, ny = places[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    visited[i] = True
                    q.append(i)
    return "sad"


t = int(input())

for _ in range(t):
    n = int(input())
    places = []

    for _ in range(n+2):  
        x, y = map(int, input().split())
        places.append((x, y))
    print(bfs(places))
