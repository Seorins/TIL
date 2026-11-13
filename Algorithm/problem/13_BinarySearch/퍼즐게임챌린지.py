def check(level, times, diffs, limit):
    total = 0

    for i in range(len(diffs)):
        if diffs[i] <= level:
            total += times[i]
        else:
            total += ((diffs[i] - level) * (times[i]+times[i-1])) + times[i] 

    return total <= limit

def solution(diffs, times, limit):
    
    l, r = 1, max(diffs)
    answer = 0
    
    while l <= r:
        mid = (l+r) // 2
        
        if check(mid, times, diffs, limit):
            answer = mid
            r = mid-1
            
        else: 
            l = mid+1
    
    return answer
    