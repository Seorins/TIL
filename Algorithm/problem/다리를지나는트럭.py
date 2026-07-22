# 고려 요건 : 길이, 무게 
# 최소 몇 초가 걸리는지 return 
# 먼저 들어온 게 먼저 나감 = queue로 관리 
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    now_weight = 0
    trucks = deque(truck_weights) # 대기열
    bridge = deque([0] * bridge_length)  # 다리  
    
    # 다리 위에 있는 트럭도 처리 필요
    while trucks or now_weight > 0: 
        time += 1
        
        # 다리 무게 관리 
        out = bridge.popleft()
        now_weight -= out
        
        # 올라올 수 있을 때 
        if trucks and now_weight + trucks[0] <= weight :
            truck = trucks.popleft()
            bridge.append(truck)
            now_weight += truck
        
        else: 
            bridge.append(0)
        
    return time
        