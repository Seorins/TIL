def solution(name):
    cnt = 0
    
    # 1. 알파벳 변경 횟수
    for n in name:
        num = min(ord(n) - ord('A'), 91 - ord(n))
        cnt += num
    
    # 2. 커서 이동 횟수
    n = len(name)
    move = n - 1
    
    for i in range(n):
        j = i + 1
        
        while j < n and name[j] == 'A':
            j += 1
        
        # 오른쪽으로 갔다가 돌아오는 경우
        right_left = 2 * i + n - j
        
        # 왼쪽으로 갔다가 돌아오는 경우
        left_right = i + 2 * (n - j)
        
        move = min(move, right_left, left_right)
    
    return cnt + move