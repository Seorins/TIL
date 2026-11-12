from collections import deque

def solution(cards1, cards2, goal):
    # O(N^3)까지도 가능
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for st in goal:
        if cards1 and cards1[0] == st:
            cards1.popleft()
        
        elif cards2 and cards2[0] == st:
            cards2.popleft()
            
        else: 
            return "No"
    
    return "Yes"