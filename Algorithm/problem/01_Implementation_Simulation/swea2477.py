'''
N개의 접수 창구 M개의 정비 창구 (1부터)

시간 : 접수 창구 ai / 정비 창구 bj 

방문 고객 K명
k 고객이 차량 정비소 도착 시간 tk

[접수 창구]
1. 고객 번호 낮은 순서대로 우선 접수
2. 빈 창구 여러곳일 경우 창구 번호가 작은 곳으로

[정비 창구]
1. 먼저 기다리는 고객 우선
2. 동시에 할 경우 접수 창구번호가 작은 고객부터
3. 빈 창구 여러 곳일 경우 정비 창구 번호 작은 곳

=> 지갑을 분실한 고객과 같은 접수창구와 잡이창구를 이용한 고객의 고객번호를 찾아 합을 출력
없을 경우 -1

완전 스케줄링 느낌 아님..?
'''

T = int(input())

for tc in range(1, T + 1):
    n, m, k, A, B = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    t_lst = list(map(int, input().split()))

    # 각각 끝나는 시간
    rec_end = [-1] * n
    fix_end = [-1] * m

    # 고객이 사용한 창구 번호
    rec_use = [0] * k
    fix_use = [0] * k

    repair_wait = [] # 정비 대기


    # 접수 
    for person in range(k):
        done = False

        # 빈 접수 창구 있을 경우에는 바로 배정 
        for i in range(n):
            if rec_end[i] < t_lst[person]:
                rec_end[i] = t_lst[person] + ai[i] - 1
                rec_use[person] = i
                repair_wait.append([rec_end[i] + 1, i, person])
                done = True
                break
        
        # 없으면 가장 빨리 끝나는 창구로 
        if not done:
            i = rec_end.index(min(rec_end))
            rec_end[i] += ai[i]
            rec_use[person] = i
            repair_wait.append([rec_end[i] + 1, i, person])

    
    # 접수 완료 시간 / 접수 창구 번호 기준으로 순서 정렬
    repair_wait.sort()


    # 정비
    for ready, rec_idx, person in repair_wait:
        done = False

        # 빈 장비 창구 있으면 바로 배정
        for j in range(m):
            if fix_end[j] < ready:
                fix_end[j] = ready + bj[j] - 1
                fix_use[person] = j
                done = True
                break

        # 빈 창구 없을 때 빨리 끝나는 거 배정
        if not done:
            j = fix_end.index(min(fix_end))
            fix_end[j] += bj[j]
            fix_use[person] = j

    result = 0
    for i in range(k):
        if rec_use[i] + 1 == A and fix_use[i] + 1 == B:
            result += (i + 1)

    if result == 0:
        result = -1

    print(f"#{tc} {result}")
