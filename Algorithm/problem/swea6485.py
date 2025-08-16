T = int(input())

for testcase in range(1, T + 1):
    N = int(input())
    bus_root = []
    result = []

    for _ in range(N):
        x, y = map(int, input().split())
        bus_root.append([x, y])
    # print(bus_root)

    P = int(input())

    bus_list = [0] * 5001

    for start, end in bus_root:
        # print(start, end) 1 3 / 2 5
        for i in range(start, end + 1):
            bus_list[i] += 1

    for _ in range(P):
        cnt = int(input())  # 보고싶은 정류장 번호
        result.append(bus_list[cnt])

    print(f"#{testcase} {' '.join(map(str, result))}")
