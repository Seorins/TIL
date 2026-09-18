def solution(begin, target, words):
    
    # target이 words안에 없을 때
    if target not in words:
        return 0
    
    use = [False] * len(words)
    min_cnt = 51
    
    def dfs(word, cnt):
        nonlocal min_cnt
        
        # 종료 조건 = target 이랑 같을 때
        if word == target:
            min_cnt = min(min_cnt, cnt)
            return 
        
        for i in range(len(words)):
            # 글자 하나만 다른지 비교
            diff = sum(a != b for a, b in zip (word, words[i]))
            if diff == 1 and not use[i]:
                use[i] = True
                dfs(words[i], cnt+1)
                use[i] = False
    
    dfs(begin, 0)
                
    return 0 if min_cnt == 51 else min_cnt
                
