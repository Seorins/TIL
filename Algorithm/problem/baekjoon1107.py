def find(num):
    for n in str(num):
        if n in buttons:
            return False
    
    return True

N = int(input()) # 이동하려는 채널
M = int(input()) # 고장난 버튼 수

if M :
    buttons = list(input().split()) # 고장난 버튼 목록
else:
    buttons = []

min_cnt = abs(N-100) # 최악의 경우(+, -만 누를 수 있음)

for num in range(999999):
    if find(num):
        cnt = len(str(num)) + abs(N-num)
        min_cnt = min(min_cnt, cnt)

print(min_cnt)