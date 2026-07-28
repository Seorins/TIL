T = int(input())

for tc in range(1, T+1):
    M, A = map(int, input().split()) # 총 이동시간 / BC 개수

    # 이동 정보 (0초 추가)
    A_move = [0] + list(map(int, input().split()))
    B_move = [0] + list(map(int, input().split()))

    # BC 개수
    BC = [list(map(int, input().split())) for _ in range(A)]


    # 초기 위치
    ax, ay = 1, 1
    bx, by = 10, 10

    # 이동X, 상, 우, 하, 좌
    dx = [0, 0, 1, 0, -1]
    dy = [0, -1, 0, 1, 0]

    # 좌표별 가능한 BC 기록
    # 대각선 부분도 결국 step 수만 같으면 됨 
    # 해당 step 내 속하는 지 확인
    graph = [[[] for _ in range(11)] for _ in range(11)]

    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(A):
                x, y, c, p = BC[k]
                if abs(i-x) + abs(j-y) <= c:
                    graph[i][j].append(k)



    total = 0

    for i in range(M+1):
        # 현재 좌표 갱신
        ax += dx[A_move[i]]
        ay += dy[A_move[i]]
        bx += dx[B_move[i]]
        by += dy[B_move[i]]

        # 현재 좌표에서 가능한 후보
        A_BC = graph[ax][ay]
        B_BC = graph[bx][by]

        now = 0

        # A만 선택하기
        for i in A_BC:
            now = max(now, BC[i][3])

        # B만 선택하기
        for j in B_BC:
            now = max(now, BC[j][3])
    
        # A, B 둘다 선택하기 
        for i in A_BC:
            p = BC[i][3]
            for j in B_BC:
                if i == j:
                    val = p
                else:
                    val = p + BC[j][3]
                if val > now:
                    now = val


        total += now
    print(f"#{tc} {total}")


