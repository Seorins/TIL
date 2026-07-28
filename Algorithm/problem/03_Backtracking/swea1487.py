import sys
sys.stdin = open('input.txt', 'r')
# N개의 집합에서 부분집합의 합이 S가 되는 경우의 수

def powerset(total, cnt):
    global a_cnt

    if total == S:
        a_cnt += 1
        return 

    # 가지치기 생각 좀 하쟈잇!!!!!
    if cnt == N or total > S:
        return 
    
    powerset(total+numbers[cnt], cnt+1)
    powerset(total, cnt+1)


T = int(input())
for tc in range(1, T+1):
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    a_cnt = 0

    powerset(0, 0)

    print(f"#{tc} {a_cnt}")




