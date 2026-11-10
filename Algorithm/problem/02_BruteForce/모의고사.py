def solution(answers):
    first = [1, 2, 3, 4, 5] # 5
    second = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10    
    scores = [0] * 3
    
    for idx, a in enumerate(answers) : 
        if first[idx%5] == a : 
            scores[0] += 1
            
        if second[idx%8] == a : 
            scores[1] += 1
            
        if third[idx%10] == a : 
            scores[2] += 1
            
    max_score = max(scores)
    
    answer = []

    for i, score in enumerate(scores) : 
        if max_score == score : 
            answer.append(i+1)
            
    return answer


# -----------------------------------------------------------------

def solution(answers):
    patterns = [[1, 2, 3, 4, 5], 
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    result = [0] * 3
    
    for i, val in enumerate(answers):
        for j, val2 in enumerate(patterns):
            if val == val2[i % len(patterns[j])]:
                result[j] += 1
            
    max_score = max(result)
    scores = []
    
    for idx, r in enumerate(result):
        if r == max_score:
            scores.append(idx+1)
            
    return scores