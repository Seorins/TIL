T = int(input())

for testcase in range(1, T + 1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]

    # M*1 1*M
    # 양쪽 글이 같아야 함

    fin_word = ""

    # 가로 찾기
    for i in range(N):
        for j in range(N - M + 1):
            word = "".join(words[i][j : j + M])
            if word == word[::-1]:
                fin_word = word

    # 세로 찾기
    for j in range(N):
        for i in range(N - M + 1):
            word = "".join(words[i + k][j] for k in range(M))
            if word == word[::-1]:
                fin_word = word

    print(f"#{testcase} {fin_word}")
