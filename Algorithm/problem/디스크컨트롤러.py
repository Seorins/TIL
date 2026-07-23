import heapq

def solution(jobs):
    waiting = [] # 대기열
    cur_time = 0 # 현재 시간
    return_time = 0 # 반환 시간
    job_idx = 0 # 작업 위치
    completed = 0 # 완료 작업
    
    # 소요시간 순으로 정렬 (작업 번호 추가)
    jobs = [(i, j, idx) for idx, (i, j) in enumerate(jobs)]
    jobs.sort()
    
    while (completed < len(jobs)) :
        # 대기열에 넣기
        while (job_idx < len(jobs) and jobs[job_idx][0] <= cur_time) : 
            
            # 대기열 우선순위에 맞게 저장
            req, dur, idx = jobs[job_idx]
            heapq.heappush(waiting, (dur, req, idx))
            
            job_idx += 1
            
            cur_time 
            
        # 작업할 게 있다면
        if waiting :
            dur, req, idx = heapq.heappop(waiting)
            cur_time += dur
            return_time += cur_time - req
            completed += 1
        
        # 없을 경우 작업 안한 애 시간으로 
        else : 
            cur_time = jobs[job_idx][0]
            
    return return_time // completed