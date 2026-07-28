T = int(input())

def find_page(N, page):
    l = 1
    r = N
    cnt = 0

    while l <= r:
        cnt += 1
        middle = (l + r) // 2
        if middle == page:
            return cnt

        elif middle > page:
            r = middle

        else:
            l = middle


for testcase in range(1, T + 1):
    P, A, B = map(int, input().split())

    A_cnt = find_page(P, A)
    B_cnt = find_page(P, B)

    if A_cnt < B_cnt:
        result = "A"
    elif B_cnt < A_cnt:
        result = "B"
    else:
        result = 0

    print(f"#{testcase} {result}")
