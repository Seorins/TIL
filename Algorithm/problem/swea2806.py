T = int(input())

def dfs(row):
    global count 
    if row == N : 
        count += 1
        return 
    
    for j in range(N):
        if not col[j] and not diag1[row+j] and not diag2[row-j+N-1]:
            col[j] = diag1[row+j] = diag2[row-j+N-1] = True
            dfs(row+1)
            col[j] = diag1[row+j] = diag2[row-j+N-1] = False
        

for tc in range(1, T+1):
    N = int(input()) # N*N보드에 N개의 퀸

    col = [False] * N 
    diag1 = [False] * (2*N-1)
    diag2 = [False] * (2*N-1)

    count = 0

    dfs(0)
    print(f"#{tc} {count}")