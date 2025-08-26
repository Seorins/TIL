T = 10

for testcase in range(1, T + 1):
    dump_cnt = int(input())
    box_height = list(map(int, input().split()))

    for i in range(dump_cnt):

        box_height.sort()
        box_height[0] += 1
        box_height[-1] -= 1

    minus_height = max(box_height) - min(box_height)

    print(f"#{testcase} {minus_height}")
