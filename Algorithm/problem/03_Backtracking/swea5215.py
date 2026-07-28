def recur(idx, cal, score):
    global max_score

    if cal > L:
        return

    if idx == N:
        max_score = max(max_score,score)
        return

    # 선택할 떄
    recur(idx+1, cal + food[idx][1], score + food[idx][0])

    # 선택하지 않을 떄
    recur(idx+1, cal, score)

T = int(input())

for tc in range(1, T+1):
    # N = 재료의 수 
    # L = 제한 칼로리 
    N, L = map(int, input().split())
    # 재료에 대한 민기의 맛에 대한 점수 / 칼로리 
    food = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0

    recur(0, 0, 0)
    
    # 가장 맛있는 햄버거의 점수 구하기
    print(f"#{tc} {max_score}")

