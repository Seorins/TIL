T = int(input())

for testcase in range(1, T+1):
    str1 = input() # 작은 문자열
    str2 = input() # 긴 문자열

    N = len(str1)
    M = len(str2)

    # 일치하는 부분이 없다고 가정
    answer = 0

    for i in range(M-N+1):
        cnt = 0
        for j in range(N):
            if str2[j+i] == str1[j]:
                cnt += 1
        if cnt == N:
            answer = 1

    print(f"#{testcase} {answer}")