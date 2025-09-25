N = 10
p = [i for i in range(N+1)]
ranks = [0] * (N+1)

def find_set(x):
    if x == p[x]:
        return x

    p[x] = find_set(p[x])
    return p[x]