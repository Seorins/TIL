# 맥주 한 박스에는 20병
# 한 병으로 50m 이동
# 최대 1000m 이동 가능
# 편의점에 가서 다시 맥주를 채울 수 있음 
# 결국 |x1 - x2| + |y1 - y2| 가 1000 이하이면 가능! 

from collections import deque

def bfs(places):
    visited = [False] * len(places)
    q = deque([0]) 
    visited[0] = True

    while q:
        cur = q.popleft()
        x, y = places[cur]
        
        #  축제 좌표 
        nx, ny = places[-1]

        # 현재 위치 - 축제가 1000 이하이면 바로 happy
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
