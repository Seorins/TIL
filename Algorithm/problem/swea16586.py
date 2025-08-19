T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    min_num = float('inf')

    
    print(f"#{tc} {min_num}")
