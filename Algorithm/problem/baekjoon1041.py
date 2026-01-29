N = int(input())
arr = list(map(int, input().split()))

ans = 0

if N == 1:
    arr.sort()
    ans = sum(arr[:5])
else:
    a = min(arr[0], arr[5])
    b = min(arr[1], arr[4])
    c = min(arr[2], arr[3])

    mins = sorted([a, b, c])

    min1 = mins[0]
    min2 = mins[0] + mins[1]
    min3 = mins[0] + mins[1] + mins[2]

    n1 = 4 * (N - 2) * (N - 1) + (N - 2) ** 2
    n2 = 4 * (N - 1) + 4 * (N - 2)
    n3 = 4

    ans = min1 * n1 + min2 * n2 + min3 * n3

print(ans)
