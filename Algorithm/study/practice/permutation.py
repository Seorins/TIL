# 중복 순열
# 0, 1, 2 3개의 카드 존재 => 2개를 뽑음

path = [] # used, visited ... --> 뽑은 카드들을 저장

# 기저조건(종료조건) : 2개의 카드를 모두 뽑았다면 종료
# - 시작점 : 0개의 카드를 고른 상태부터 시작
# 다음 재귀호출 구조 : [0, 1, 2] 카드 중 하나를 고름

# 중복 o
def recur(cnt):
    if cnt == 2:
        print(*path)        
        return
    
    for num in range(3):
        path.append(num)
        recur(num+1)
        path.pop()

    # # 카드 0, 1, 3 중 하나를 선택 
    # path.append(0)
    # recur(cnt + 1) # 하나 선택했으니 다음 선택으로 이동
    # path.pop()

    # path.apend(1)
    # recur(cnt + 1)
    # path.pop()

    # path.append(2)
    # recur(cnt + 1)
    # path.pop()

recur(0)