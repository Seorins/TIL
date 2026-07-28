from collections import Counter

def solution(participant, completion):
    cnt = Counter(participant) - Counter(completion)
    
    return list(cnt.keys())[0]