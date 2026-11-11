def solution(N, stages):
    counts = [0] * (N+2)
    
    for s in stages:
        counts[s] += 1
        
    fails = {}
    total = len(stages)
    
    for i in range(1, N+1):
        if counts[i] == 0:
            fails[i] = 0
        
        else:
            fails[i] = counts[i] / total
            total -= counts[i]
    
    results = sorted(fails, key=lambda x: (-fails[x], x))
      
    return results