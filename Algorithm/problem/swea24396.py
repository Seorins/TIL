T = int(input())

for tc in range(1, T+1):
    # B = 검은 공, W = 흰공 
    # B = 검은 상자, W = 흰 상자
    # 모든 공을 상자에 담아서 모든 상자가 정확히 한 개의 공을 담고자 함
    # 검은 상자에 검은 공 X점
    # 흰 상자에 흰 공 Y점
    # 반대로 들어 있으면 Z점
    B, W, X, Y, Z = map(int, input().split())

    # 모든 상자의 점수의 합을 최대화 => 최대 점수 구하기
    # 2 2 1 1 0 => 4
    
    # 풀이 방법 -> 점수가 큰 것대로 거기에 제일 많은 공을 갖다 넣기

    scores = {'x' : X, 'y' : Y, 'z': Z}
    max_num = -float('inf')

    for i in scores:
        max_num = max(scores[i], max_num)
        



    





