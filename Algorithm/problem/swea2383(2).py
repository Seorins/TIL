'''
N x N 격자
사람 여러 명 / 계단 2개

각 사람은 두 계단 중 하나 선택

1. 계단까지 맨해튼 거리 이동
2. 도착 후 1분 뒤부터 내려감
3. 계단에는 동시에 최대 3명
4. 계단 길이 K만큼 시간 걸림
5. 꽉 차 있으면 먼저 끝나는 사람 나갈 때까지 대기

→ 모든 사람이 다 내려가는 시간의 최솟값 구하기
'''

from collections import deque

def simulate(arrivals, stair_len):
    if not arrivals:
        return 0

    end = deque()
    last = 0

    for dist in arrivals:
        start = dist + 1

        if len(end) == 3:
            start = max(start, end.popleft())

        end_time = start + stair_len
        end.append(end_time)
        last = end_time

    return last


def calculate(select):
    dist = [[], []]

    # 미리 계산된 거리 사용
    for i in range(len(select)):
        dist[select[i]].append(pre_dist[i][select[i]])

    times = []

    for stair_idx in range(2):
        if not dist[stair_idx]:
            times.append(0)
            continue

        stair_len = stair_len_list[stair_idx]
        dist[stair_idx].sort()

        t = simulate(dist[stair_idx], stair_len)

        # 가지치기
        if t >= min_time:
            return t

        times.append(t)

    return max(times)


def recur(idx):
    global select, min_time

    if idx == len(people):
        min_time = min(min_time, calculate(select))
        return

    # 0번 계단
    select.append(0)
    recur(idx + 1)
    select.pop()

    # 1번 계단
    select.append(1)
    recur(idx + 1)
    select.pop()


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stair = []
    select = []
    min_time = float('inf')

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                people.append((i, j))
            
            elif graph[i][j] > 1:
                stair.append((i, j))

    pre_dist = [[0, 0] for _ in range(len(people))]
    stair_len_list = []

    for s_idx in range(2):
        sr, sc = stair[s_idx]
        stair_len_list.append(graph[sr][sc])
        
        for p_idx in range(len(people)):
            pr, pc = people[p_idx]
            pre_dist[p_idx][s_idx] = abs(pr - sr) + abs(pc - sc)

    recur(0)

    print(f"#{tc} {min_time}")