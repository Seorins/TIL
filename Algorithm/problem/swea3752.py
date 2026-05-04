T = int(input())
 
for tc in range(1, T+1):
    n = int(input())
    scores = list(map(int, input().split()))
    get = [0]
    visited = [True] + [False] * sum(scores)
    
    for score in scores:
        for i in range(len(get)):
            if not visited[score + get[i]]:
                visited[score + get[i]] = True
                get.append(score + get[i])
                
    print(f"#{tc} {len(get)}")