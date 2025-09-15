def make_set(n):
    parents = [i for i in range(n+1)]
    return parents


def find_set(x):
    if x == parents[x]:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y :
        return
    
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = make_set(N)

    for i in range(0, len(arr)-1, 2):
        union(arr[i], arr[i+1])


    groups = set()
    for r in range(1, len(parents)):
        groups.add(find_set(r))


    cnt = len(groups)
    print(f"#{tc} {cnt}")