T = int(input())
result = []

for i in range(T):
    K, N, M = map(int, input().split())
    busstop_num = list(map(int, input().split()))

    bus_station = [0] * (N + 1)

    for num in busstop_num:
        bus_station[num] = 1

    arrived = 0
    now = 0

    while K + now < N:
        for j in range(K, 0, -1):
            if bus_station[now + j] == 1:
                now += j
                arrived += 1
                break

        else:
            arrived = 0
            break

    result.append(f"#{i+1} {arrived}")


for r in result:
    print(r)
