for testcase in range(1, 11):
    N = int(input())
    graph = [list(input()) for _ in range (100)]

    max_len = 0

    # 길이를 늘려가면서 가장 긴 회문 찾기
    for m in range(1, 101):
        for i in range(100):
            for j in range(100-m+1):
                sub_arr = []
                for c in range(m):
                    sub_arr.append(graph[i][j+c])
                        
                if sub_arr == sub_arr[::-1]:
                    if max_len < m : 
                        max_len = m

    for m in range(1, 101):
        for j in range(100):
            for i in range(100-m+1):
                sub_arr = []
                for c in range(m):
                    sub_arr.append(graph[i+c][j])
                        
                if sub_arr == sub_arr[::-1]:
                    if max_len < m : 
                        max_len = m


    print(f"#{N} {max_len}")