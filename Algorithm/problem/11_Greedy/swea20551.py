T = int(input())

for testcase in range(1, T+1):
    A, B, C = map(int, input().split())
    
    answer = float('inf')

    # 완전탐색 ==> runtime error
    # for a in range(1, A+1):
    #     for b in range(1, B+1):
    #         for c in range(1, C+1):
    #             if a < b < c :
    #                 after = (A-a) + (B-b) + (C-c)
    #                 answer = min(answer, after)

    # if answer == float('inf'):
    #     answer = -1




    # 테케 틀림.....
    # max_start = min(A, B-1, C-2)

    # for a in range(1, max_start + 1):
    #     b = a + 1
    #     c = a + 2
    #     after = (A-a) + (B-b) + (C-c)
    #     answer = min(answer, after)

    # if answer == float('inf'):
    #     answer = -1


    c = C
    b = min(B, c - 1)
    a = min(A, b - 1)
    
    if not (1 <= a < b < c) :
        answer = -1
    else:
        answer = (A - a) + (B - b) + (C - c)

    print(f"#{testcase} {answer}")
