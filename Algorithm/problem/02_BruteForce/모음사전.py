def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    cnt = 0
    
    def recur(cur):
        nonlocal cnt 
        
        if cur : 
            cnt += 1
            if cur == word : 
                return True
        
        if len(cur) == 5 : 
            return False 
        
        for w in words : 
            if recur(cur + w) : 
                return True
            
        return False
    
    recur('')
    
    return cnt
            

# -------------------------------------


from itertools import product

def solution(word):

    words = []
    
    for length in range(1, 6):
        for p in product("AEIOU", repeat=length):
            words.append(''.join(p))
            
    words.sort()
    
    return words.index(word) + 1