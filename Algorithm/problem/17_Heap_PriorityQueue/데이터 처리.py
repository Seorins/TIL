import heapq
0
def solution(data_size, processing_time):
    using_server = []
    waiting_server = []
    datas = []
    time = 0

    datas = [(s, t + i) for i, s, t in enumerate(zip(data_size, processing_time))]  