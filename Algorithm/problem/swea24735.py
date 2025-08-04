N = int(input())
boxs = list(map(int, input().split()))
max_cnt = 0

for i in range(N):
    cnt = 0
    for j in range(N - i):
        if boxs[i] > boxs[j]:
            cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

print(max_cnt)
