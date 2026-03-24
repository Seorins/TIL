import sys
input = sys.stdin.readline

N = int(input())
lst = input()

stack = [] 
cnt = [0] * N 
ans = 0
max_ans = 0

for i in range(N):
    if lst[i] == "(": 
        stack.append(i)

    else:
        if stack:
            cnt[i] = cnt[stack[-1]] = 1 

# 연속적인 1이 얼마나 있는지 체크
for c in cnt: 
    if c == 1: 
        ans += 1 
        max_ans = max(max_ans, ans) 
    else: 
        ans = 0
print(max_ans)