path = [] 
used = [False] * 7 # 고를 수 있는 수 + 1만큼 고르기 (0은 버릴려고 )


# 중복 x
def recur(cnt):
    if cnt == 3:
        print(*path)        
        return
    
    for num in range(1, 7):
        if used[num]:
            continue

        # in을 쓰면 리스트 전부를 확인
        # if num in path : # in => O(N) 조심해야함
        #     continue

        used[num] = True
        path.append(num)

        recur(cnt+1)

        path.pop()
        used[num] = False

recur(0)