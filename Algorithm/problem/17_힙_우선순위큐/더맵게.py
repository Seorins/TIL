# 새로운 요소가 계속 들어옴 => heap 사용 

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
  
    while (len(scoville) > 1 and scoville[0] < K) : 
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        
        cnt += 1
    
    if scoville[0] < K : 
        return -1
    
    return cnt
    