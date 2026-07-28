# heap 풀이 O(N log N)

import heapq

def solution(operations):
    min_heap = [] # 최소 힙
    max_heap = [] # 최대 힙
    valid = [False] * len(operations) # 힙 상태 관리
    
    for idx, oper in enumerate(operations) : 
        st, num = oper.split()
        
        # 큐에 각각 삽입 (고유 번호 추가)
        if st == 'I':
            heapq.heappush(min_heap, (int(num), idx))
            heapq.heappush(max_heap, (-int(num), idx))
            valid[idx] = True
            
        else:
            # 삭제하기 전에 상태 갱신 필요
            while (min_heap and not valid[min_heap[0][1]]):
                heapq.heappop(min_heap)
            
            while (max_heap and not valid[max_heap[0][1]]):
                heapq.heappop(max_heap)

            if not min_heap or not max_heap: 
                continue
            
            # 분기 처리
            if num == "1":
                _, idx = heapq.heappop(max_heap)
                valid[idx] = False
                
            else : 
                _, idx = heapq.heappop(min_heap)
                valid[idx] = False
                
    # 마지막 상태 처리
    while (min_heap and not valid[min_heap[0][1]]):
        heapq.heappop(min_heap)

    while (max_heap and not valid[max_heap[0][1]]):
        heapq.heappop(max_heap)
            
    # 결과 출력       
    if not min_heap or not max_heap: 
        return [0, 0]
    
    else:
        return [-max_heap[0][0], min_heap[0][0]]
        


# -----------------------------------------------------


# min, max 풀이 O(N²)

def solution(operations):
    numbers = []
    
    for o in operations : 
        e, n = o.split()

        if e == 'I' : 
            numbers.append(int(n))
            
        elif numbers : 
            if n == '1' : 
                numbers.remove(max(numbers))

            else : 
                numbers.remove(min(numbers))
    
    if numbers : 
        return [max(numbers), min(numbers)]
    
    else : 
        return [0, 0]

