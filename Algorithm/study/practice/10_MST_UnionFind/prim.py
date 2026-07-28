import sys
sys.stdin = open('mst_input.txt', 'r')

# 인접 행렬
from heapq import heappush, heappop

# 특정 정점 기준으로 시작
# - 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 감
# --> 작은 노드를 먼저 꺼내기 위해 우선순위 큐(heapq)를 활용
# 우선순위 큐는 정렬 기준이 앞 데이터 기준으로 해야해서 가중치를 앞에 두는 게 좋음
def prim(start_node):
    pq = [(0, start_node)] # (가중치, 노드) 형태
    MST = [0] * V # visited와 동일함
    min_weight = 0 # 최소 비용

    while pq:
        weight, node = heappop(pq) # 가장 작은 가중치 

        # 이미 방문한 노드라면 continue
        if MST[node]:
            continue

        MST[node] = 1 # node로 가는 최소 비용이 선택됨
        min_weight += weight # 누적합 추가

        for next_node in range(V):
            # 갈수 없으면 continue
            if graph[node][next_node] == 0:
                continue

            # 이미 방문했으면 continue
            if MST[next_node]:
                continue
                
            # 원래 BFS에서는 여기서 방문 처리 -> MST에서는 최소 비용이 안됨
            heappush(pq, (graph[node][next_node], next_node))


    return min_weight


V, E = map(int, input().split())

graph = [[0] * V for _ in range(V)]  # 인접 행렬 vs 인접 리스트

for _ in range(E):
    start, end , weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight # 양방향


result = prim(0)  # 출발 정점과 함께 시작
                  # 출발 정점을 바꾸어도 최소 비용은 똑같음
                  # 단, 그래프는 다르게 나올 수 있음
print(f"최소비용 = {result}")


# --------------------------------------------
# 인접 리스트 

from heapq import heappush, heappop

def prim(start_node):
    pq = [(0, start_node)]
    MST = [0] * V
    min_weight = 0

    while pq:
        weight, node = heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        # node와 연결된 모든 간선 확인
        for next_weight, next_node in graph[node]:
            if not MST[next_node]:
                heappush(pq, (next_weight, next_node))

    return min_weight


# 입력 처리
V, E = map(int, input().split())
graph = [[] for _ in range(V)]  # 인접 리스트

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))
    graph[end].append((weight, start))  # 양방향
