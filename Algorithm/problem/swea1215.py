T = 10 

for testcase in range(1, T+1):
    N = int(input()) 
    graph = [list(input()) for _ in range(8)]
    
    cnt = 0

    for i in range(8):
        for j in range(8-N+1):
            words = []
            for c in range(N):
                words.append(graph[i][j+c])
            if words == words[::-1]:
                cnt += 1

    for j in range(8):
        for i in range(8-N+1):
            words = []
            for c in range(N):
                words.append(graph[i+c][j])
            if words == words[::-1]:
                cnt += 1
             
    print(f"#{testcase} {cnt}")