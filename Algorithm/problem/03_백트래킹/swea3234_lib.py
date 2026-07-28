from itertools import permutations

def recur(idx, left, right, arr):
    global ans

    if left < right : 
        return 

    if idx == N : 
        ans += 1
        return

    recur(idx+1, left + arr[idx], right, arr)

    if left >= right + arr[idx]:
        recur(idx+1, left, right + arr[idx], arr)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for perm in permutations(arr, N):
        recur(0, 0, 0, perm)

    print(f"#{tc} {ans}")