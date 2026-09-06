def solution(numbers, target):

    cnt = 0 
    
    def dfs(n, idx):
        nonlocal cnt 

        if idx == len(numbers): 
            if n == target : 
                cnt += 1
            return 
          
        # 1. 더하기 
        dfs(n + numbers[idx], idx+1)
        
        # 2. 빼기
        dfs(n - numbers[idx], idx+1)
    
        
    dfs(0, 0)
    
    return cnt