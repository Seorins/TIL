# 0 이동x / 1 상 / 2 우 / 3 하 / 4 좌
# 같은 위치로 이동 가능 그런데 이제 같은 BC 사용하면 절반씩
# 충전량 합의 최대값 출력 
            
T = int(input())

for tc in range(1, T+1):
    M, A = map(int, input().split()) # 사용자의 이동 정보 개수 / BC 개수
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))
    
    BC = [list(map(int, input().split())) for _ in range(A)] # 위치(n,n), 충전범위, 성능(짝수)
    graph = [[0] * 10 for _ in range(10)]
    
    # 이동x 상 우 하 좌  
    mx = [0, 0, 1, 0, -1]
    my = [0, -1, 0, 1, 0] 
    
    # 시작 위치 
    A_loc = (1, 1) 
    B_loc = (10, 10)
    
    # 
    for i in range(10):
        pass