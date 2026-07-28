def calc():
    primes = [0] * 1000002
    
    for i in range(1, 1000001, 2):
        for j in range(i, 1000001, i):
            primes[j] += i
            
    for i in range(1, 1000001):
        primes[i + 1] += primes[i]
        
    return primes
 

T = int(input())

results = []
primes = calc()
    
for tc in range(1, T + 1):    
    L, R = map(int, input().split())
    
    answer = primes[R] - primes[L - 1]
    results.append(f'#{tc} {answer}\n')
    
print(''.join(results))