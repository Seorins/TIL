import sys
sys.stdin = open('input.txt', 'r')
'''
방 안의 사람들 P, 계단 입구 S

사람들이 아래층으로 이동하는 시간은 계단 입구까지 이동시간과 계단을 내려가는 시간이 포함됨

이동 시간(분) = | PR - SR | + | PC - SC |
(PR, PC : 사람 P의 세로위치, 가로위치, SR, SC : 계단 입구 S의 세로위치, 가로위치)

- 계단을 내려가는 시간은 계단 입구에 도착한 후부터 계단을 완전히 내려갈 때까지의 시간이다.
- 계단 입구에 도착하면, 1분 후 아래칸으로 내려 갈 수 있다.
- 계단 위에는 동시에 최대 3명까지만 올라가 있을 수 있다.
- 이미 계단을 3명이 내려가고 있는 경우, 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 한다.
- 계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 K 분이 걸린다.

이동이 완료되는 최소 시간 

'''

def calculate(select):
    dist = [[], []]
    time = 0

    # 계단까지 가는데 걸리는 소요시간 (계단 별로)
    # [1, 0, 0, 0, 1, 0, 1, 1]
    for i in range(len(select)):
        pr, pc = people[i]
        sr, sc = stair[select[i]]
        time = abs(pr-sr) + abs(pc-sc)
        dist[select[i]].append(time)

    
    times = []
    for stair_idx in range(2):
        if dist[stair_idx] == []:
            times.append(0)
        
        stair_len = graph[stair[stair_idx][0]][stair[stair_idx][1]]

        

    return 
 


# 사람이 계단을 사용할 수 있는 case 모두 구하기 
def recur(idx):
    global select
    global min_time

    if idx == len(people):
        min_time = min(min_time, calculate(select))
        return 
    
    for i in range(len(stair)):
        select.append(i)
        recur(idx+1)
        select.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stair = []
    select = []
    min_time = float('inf')

    # 사람 위치 구하기
    # 계단 위치 구하기
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:    
                people.append((i, j))

            if graph[i][j] != 1 and graph[i][j] != 0:
                stair.append((i, j))

    recur(0)
    print(select)


