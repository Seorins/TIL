'''
자성 다를 경우 반대 방향으로 1칸 회전 

오른쪽 접지 바퀴 번호는 top 기준 +2 
왼쪽 접지 바퀴 번호는 top 기준 +6

리스트 변형 안 시키고 top만 저장 후 가능? 
바퀴의 총 회전 횟수를 구하고 결론적으로 마지막 top만 구하면 됨 
'''

T = int(input())

for tc in range(1, T+1):       
    K = int(input()) # 회전 횟수
    magnet = [list(map(int, input().split())) for _ in range(4)]
    
    top = [0] * 4 # top 인덱스 기록
    
    for _ in range(K):
        idx, dir = map(int, input().split())
        idx -= 1  

        rotate = [0] * 4
        rotate[idx] = dir # 0 정지 1 시계 -1 반시계

        # 오른쪽 회전
        for i in range(idx, 3):
            right_i = magnet[i][(top[i] + 2) % 8]        
            left_next = magnet[i+1][(top[i+1] + 6) % 8] 

            if right_i == left_next: # 같으면 나가기 
                break
            
            rotate[i+1] = -rotate[i]  # 다르면 반대 방향 회전
            
            
        # 왼쪽 회전
        for i in range(idx, 0, -1):
            left_i = magnet[i][(top[i] + 6) % 8]         
            right_prev = magnet[i-1][(top[i-1] + 2) % 8] 

            if right_prev == left_i:
                break
            
            rotate[i-1] = -rotate[i]

        # top 계산
        for i in range(4):
            if rotate[i] == 1: # 시계
                top[i] = (top[i] - 1) % 8
            elif rotate[i] == -1: # 반시계
                top[i] = (top[i] + 1) % 8

    result = 0
    for i in range(4):
        if magnet[i][top[i]] == 1:  
            result += 2**i

    print(f"#{tc} {result}")