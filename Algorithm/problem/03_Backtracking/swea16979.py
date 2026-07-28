import sys
sys.stdin = open('input.txt', 'r')

def dfs(row, total):
    global min_total 

    # 가지치기 해라... 제발...
    if total >= min_total:
        return
    
    if row == N : 
        min_total = min(min_total, total)
        return min_total
    
    for j in range(N):
        if not col[j]:
            col[j] = True
            dfs(row+1, total + graph[row][j])
            col[j] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    min_total = float('inf')
    col = [False] * N

    dfs(0, 0)
    print(f"#{tc} {min_total}")