def paper(N):

    if N == 1:
        return 1

    elif N == 2:
        return 3
    
    else:
        return paper(N-1) + 2*paper(N-2)

    
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    result = paper(N//10)
    
    print(f"#{tc} {result}")