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
            