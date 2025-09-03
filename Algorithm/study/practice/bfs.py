from collections import deque

def bfs(graph, start):
    # 노드의 방문을 기록하기 위해서
    # len(graph)+1 을 하는 이유는 노드는 1부터 시작하기 때문에
    # 따라서 visited[0]은 안 씀
    visited = [False] * (len(graph)+1)
    # 큐에 시작점을 넣어줌
    queue = deque([start])
    # 방문 했다는 걸 표시해줌
    visited[start] = True

    while queue:
        # 제일 처음 거를 빼줌
        v = queue.popleft()
        # 실제 방문 처리
        # 보통 이 자리에서 "출력" 또는 "거리 기록" 같은 일을 수행
        print(v, end=" ") 

        # 현재 정점 v와 연결된 모든 정점 확인
        for nxt in graph[v]:
            # 아직 방문하지 않은 정점만 처리
            if not visited[nxt]:
                # 큐에 삽입 = 나중에 탐색 예약
                # 즉시 탐색하는 게 아니라 "차례가 오면 탐색하겠다"는 의미
                queue.append(nxt)
                # 큐에 넣었으니까 방문한 걸로 치겠다
                visited[nxt] = True