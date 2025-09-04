path = []
result = 0

# 파라미터로 던져주는 게 가장 효율적임 
def recur(cnt, total):
    global result

    # 기저 조건에서 많은 경우의 수를 줄일 수 있음 
    if total > 10 : 
        return 
    
    if cnt == 3:
        # if total <= 10:
        #     result += 1
        result += 1
        return
    
    for num in range(1, 7):
        total += num
        recur(cnt + 1, total + num)

recur(0, 0)


