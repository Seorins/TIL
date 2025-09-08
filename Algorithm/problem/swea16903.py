import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 컨테이너 수, 트럭 수
    container = list(map(int, input().split())) # 화물의 무게
    truck = list(map(int, input().split())) # 트럭의 적재 용량

    # 트럭 당 적재용량 내 한 개의 컨테이너 운반 
    container.sort(reverse=True)
    truck.sort(reverse=True)
    # print(container)
    # print(truck)
    
    # 그럼 적재용량이 큰 애가 들 수 있는 가장 무거운 걸 들게 차례로 하면 안되나? 
    cnt = 0
    for i in range(len(truck)):
        for j in range(len(container)):
            if truck[i] >= container[j]:
                cnt += container[j]
                container.pop(j)
                break

    print(f"#{tc} {cnt}")