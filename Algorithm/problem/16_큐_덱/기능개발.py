# 100%일 때 서비스 반영
# 개발 속도는 다르지만 배포 순서에 맞게 배포
# 각 배포마다 몇 개 기능 배포되는지 
import math

def solution(progresses, speeds):
    
    # 1. 각각 얼마나 필요한 지 날짜부터 계산
    days = []
    answer = []
    
    for progress, speed in zip(progresses, speeds):
        days.append(math.ceil((100-progress)/speed))
        
    index = 0
    cnt = 0
    for i in range(len(days)):
        if days[index] >= days[i]:
            cnt += 1
            continue
        
        answer.append(cnt)
        cnt = 1
        index = i
    
    answer.append(cnt)
    
    return answer