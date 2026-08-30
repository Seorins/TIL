def solution(n, lost, reserve):
    cnt = n - len(lost)

    # 도난 당한 친구는 못 빌려줌
    for stu in lost[:] :      
        if stu in reserve : 
            cnt += 1 
            reserve.remove(stu)
            lost.remove(stu)
            
    for stu in lost[:] : 
        if (stu-1) in reserve :
            cnt += 1
            reserve.remove(stu-1)
            continue
            
        elif (stu+1) in reserve :
            cnt += 1
            reserve.remove(stu+1)
            continue
        
    return cnt 