from itertools import permutations

def solution(numbers):
    
    answer = set()
    
    def prime(num):
        
        if num < 2 : 
            return False

        for n in range(2, int(num**0.5)+1) : 
            if num % n == 0:
                return False

        return True
        
    
    for i in range(1, len(numbers)+1):
        for p in (permutations(numbers, i)):
            number = int(''.join(p))
           
            if prime(number):
                answer.add(number)
                
    return len(answer)