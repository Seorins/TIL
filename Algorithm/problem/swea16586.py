def backtracking(row, num):
    global min_num

    if row == N:
        min_num = min(min_num, num)
        return 

    if min_num <= num :
        return 

    for col in range(N):
        if not visited[col]:
            visited[col] = True
            backtracking(row+1, num + graph[row][col])
            visited[col] = False
        
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N 
    min_num = float('inf')

    backtracking(0, 0)

    print(f"#{tc} {min_num}")
