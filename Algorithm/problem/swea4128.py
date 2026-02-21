'''
두 명의 손님, N개의 식재료
식재료를 각각 N/2 나누어 두 개의 요리 
A, B음식은 맛의 차이가 최소가 되도록 재료 배분
식재료끼리 시너지 발생 Sij
음식의 맛은 시너지들의 합
음식 간의 맛의 차이가 최소가 되는 경우 찾기 
'''

def recur(idx, cnt):
    global min_diff

    if cnt == N // 2: 
        B_food = [i for i in range(N) if i not in A_food]
        # 음식 맛 계산(시너지 총합)
        A_taste = calc_synergy(A_food)
        B_taste = calc_synergy(B_food)
        min_diff = min(min_diff, abs(A_taste - B_taste))
        return 
        
    if idx >= N:
        return

    # 가지치기 
    if cnt + (N - idx) < N // 2:
        return

    A_food.append(idx)
    recur(idx+1, cnt+1)
    A_food.pop()

    recur(idx+1, cnt)


def calc_synergy(food):
    total = 0
    
    for i in range(len(food)):
        for j in range(i+1, len(food)):
            total += synergy[food[i]][food[j]] + synergy[food[j]][food[i]]

    return total 

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 식재료
    synergy = [list(map(int, input().split())) for _ in range(N)]

    # 하나의 음식이 재료를 가지면 다른 음식은 나머지 재료
    A_food = []

    min_diff = float('inf')

    recur(0, 0)

    print(f"#{tc} {min_diff}")

