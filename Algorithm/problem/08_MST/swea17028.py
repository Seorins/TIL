def find_set(x):
    if p[x] == x:
        return x
    
    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry : 
        return 
    
    p[rx] = ry


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    
    edges = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))

    edges.sort(key=lambda x : x[2])

    p = [i for i in range(V+1)]

    cnt = 0
    result = 0
    for s, e, w in edges:
        if find_set(s) != find_set(e):
            union(s, e)
            cnt += 1
            result += w

            if cnt == V:
                break


    print(f"#{tc} {result}")