# 시간 복잡도 O(N²)

def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j] :
                break
            
        answer.append(cnt)
        
    return answer

            
# ---------------------------------------------

# 시간 복잡도 O(N)

def solution(prices):
    answer = [0] * len(prices)
    stack = [] # 이전 인덱스들 저장
    
    for i in range(len(prices)):
        # stack 최근 가격과 비교해서 떨어졌을 경우 answer에 갱신(계속 해줘야 함)
        while(stack and prices[stack[-1]] > prices[i]) :
            prev_idx = stack.pop()
            answer[prev_idx] = i - prev_idx
            
        stack.append(i)
    
    # 떨어지지 않은 애들 처리 
    last = len(prices) -1 
    
    for i in stack : 
        answer[i] = last - i
        
    return answer
            
            