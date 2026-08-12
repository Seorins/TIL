# 완전탐색

from itertools import permutations

def solution(k, dungeons):

    max_cnt = 0 
    
    for dungeon in permutations(dungeons, len(dungeons)):
        cnt = 0
        health = k
        for need, use in dungeon: 
            if health >= need : 
                health -= use 
                cnt += 1
                
            else: 
                break
        
        max_cnt = max(max_cnt, cnt)
        
    return max_cnt



# ------------------------------------------------


# dfs

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0
    
    def dfs(health, cnt):
        nonlocal answer
        
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            need, use = dungeons[i]
            
            if not visited[i] and health >= need : 
                visited[i] = True
                
                dfs(health - use, cnt + 1)
                
                visited[i] = False
        
    dfs(k, 0)
    
    return answer