import heapq

def solution(data_size, processing_time):
    using_server = []   # (사용 가능 시간, 누적 사이즈)
    waiting_server = [] # (누적 사이즈, 사용 가능 시간)
    time = 0

    datas = [(s, t + i) for i, (s, t) in enumerate(zip(data_size, processing_time))]

    for data in datas:
        d_size, d_time = data

        # 현재 시간에 사용 가능해진 서버 관리
        while using_server and time == using_server[0][0] :
            u_time, u_size = heapq.heappop(using_server)
            heapq.heappush(waiting_server, (u_size, u_time))

        # 대기 중인 서버가 있다면
        if waiting_server:
            w_size, _ = heapq.heappop(waiting_server)
            heapq.heappush(using_server, (d_time, w_size + d_size))

        # 대기 중인 서버가 없다면 새 서버 생성
        else:
            heapq.heappush(using_server, (d_time, d_size))

        time += 1

    max_size = 0

    for i in range(len(using_server)):
        max_size = max(max_size, using_server[i][1])

    for i in range(len(waiting_server)):
        max_size = max(max_size, waiting_server[i][0])

    return max_size