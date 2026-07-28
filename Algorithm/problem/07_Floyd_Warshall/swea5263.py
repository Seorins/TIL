T  = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 인접 행렬
    g = [list(map(int, input().split())) for _ in range(N)]

    # 플로이드워샬
    # 모든 노드 쌍 사이의 최단 거리 구하기
    # 음수 가중치 가능

    # 다익스트라
    # 정해진 시작 노드에서 다른 노드까지의 최단 거리 구하기
    # 음수 가중치 불가능
    
    # 거리 저장 배열
    # dists[i][j] => i번 정점에서 j번 정점까지의 최단 거리
    dists = [[float('inf') for _ in range(N)] for _ in range(N)]

    # 경유지가 없는 경우의 최단거리 초기화
    # 인접 행렬을 참구해서 처음 최단 거리 설정
    for i in range(N):
        for j in range(N):


            # i번 정점과 j번 정점 경유지가 없는 경우 최단 거리
            # 나중에 경유지를 추가하면서 최단 거리비교를 통해 갱신
            if g[i][j] != 0 :
                dists[i][j] = g[i][j]

    
    # 플로이드 워샬 알고리즘
    # 기존 (i, j) 사이의 최단거리와 경유지 k 정점을 거쳤을 경우 최단거리 비교 => 더 작은 값 선택
    # dists[i][j] = min(dists[i][k] + dists[k][j] , dists[i][j])
    # DP 방식
    # 중간 경유지 정점 번호 K의 범위를 점점 늘려가면서 비교 
    # 경유지가 없는 경우 최단거리 dists 초기화

    # k = 0 : 경유지가 0번인 경우
    # 경유지가 없는 경우 vs 경유지가 0번인 경우 최단거리를 구하면 됨

    # k = 1 : 경우지가 1번인 경우
    # 경유지가 없는 경우, 경유지가 0번인 경우 vs 경유지가 1번인 경우 최단거리를 구하면 됨

    # k = n-1 : 모든 가능한 경유지를 고려

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dists[i][j] = min(dists[i][k] + dists[k][j] , dists[i][j])


    # 자기 자신까지의 거리는 0
    for i in range(N):
        dists[i][i] = 0

    
    max_v = max([max(i_lst) for i_lst in dists])

    # max_v = -float('inf')

    # for i in range(N):
    #     for j in range(N):
    #         if max_v < dists[i][j] : 
    #             max_v = dists[i][j]

    print(f"#{tc} {max_v}")