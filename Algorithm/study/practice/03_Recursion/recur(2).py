arr = ['O', 'X']
name = ['MIN', 'CO', 'TIM']
path = []

def recur(cnt):
    
    # 종료 조건(3명을 모두 고려)
    if cnt == 3:
        print(*path)
        return 

    # 재귀호출 파트
    # 부분집합에 포함되는 경우와 (O를 추가) 
    path.append(arr[0])
    recur(cnt + 1)
    path.pop()

    # 포함되지 않는 경우 (X를 추가)
    path.append(arr[1])
    recur(cnt + 1)
    path.pop()

recur(0) # 0명을 고려한 상태로 시작

# ------------------------------------------------------

name = ['MIN', 'CO', 'TIM']

# 두 번째 선택에서는
# 'MIN'이라는 친구가 포함된 상태를 저장하면서 
def recur(cnt, subset):
    
    if cnt == 3:
        print(*subset)
        return
    
    # 부분집합에 포함 시키는 경우
    recur(cnt + 1, subset + [name[cnt]])
    # 포함시키지 않는 경우
    recur(cnt + 1, subset)
    
recur(0, [])