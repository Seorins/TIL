# 초 시간 변환 함수
def time_change(t):
    m, s = map(int, t.split(":"))
    return m * 60 + s

def solution(video_len, pos, op_start, op_end, commands):
    
    # 시간 변환(초)
    pos = time_change(pos)
    op_start = time_change(op_start)
    op_end = time_change(op_end)
    video_len = time_change(video_len)

    for command in commands:
        # 오프닝 범위 안인지
        if op_start <= pos <= op_end:
            pos = op_end
        
        # prev일 경우
        if command == "prev":
            pos = max(0, pos-10)
            
        # next일 경우
        else:
            pos = min(video_len, pos+10)
                
    # commands 끝나고 범위 안에 있는지 마지막 한 번 확인(테케2의 경우)
    if op_start <= pos <= op_end:
            pos = op_end
    
    return f"{pos//60:02d}:{pos%60:02d}"