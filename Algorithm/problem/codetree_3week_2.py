n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 행복한 수열 = 연속하여 M개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
# 행과 열을 다 봐서 행복한 수열의 개수를 세기
# M개 이상 나오면 됨 
total = 0

# row만 보기
row = [] 
for i in range(n):
    r = grid[i]
    row.append(r)

for r in row:
    cnt = [[]]
    for c in range(n-1):
        if r[c] == r[c+1]:
            cnt[-1].append(1)
        else :
            cnt.append([])
    
    print(cnt)


# col만 보기 
col = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(grid[i][j])
    col.append(temp)

for c in col:
    cnt = [[]]
    for x in range(n-1):
        if c[x] == c[x+1]:
            cnt[-1].append(1)
        else :
            cnt.append([])
    
    print(cnt)

print(total)
