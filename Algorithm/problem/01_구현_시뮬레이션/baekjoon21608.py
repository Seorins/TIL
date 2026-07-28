import sys

input = sys.stdin.readline

n = int(input())
data = [[0] * n for _ in range(n)]

# 학생 번호 + 좋아하는 학생 4명
students = [list(map(int, input().split())) for _ in range(n ** 2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 학생 순서대로 자리 배치
for student in students:
    available = []

    for i in range(n):
        for j in range(n):
            # 빈 자리만 확인
            if data[i][j] == 0:
                prefer = 0
                empty = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        # 좋아하는 학생이 인접하면 증가
                        if data[nx][ny] in student[1:]:
                            prefer += 1

                        # 빈 자리가 인접하면 증가
                        if data[nx][ny] == 0:
                            empty += 1

                available.append((i, j, prefer, empty))

    # 좋아하는 학생 수, 빈 자리 수, 행, 열 순으로 정렬
    available.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))

    # 가장 조건에 맞는 자리에 배치
    data[available[0][0]][available[0][1]] = student[0]

answer = 0
score = [0, 1, 10, 100, 1000]

# 학생 번호 순서대로 정렬
students.sort()

# 만족도 계산
for i in range(n):
    for j in range(n):
        count = 0

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                # 좋아하는 학생이 인접하면 증가
                if data[nx][ny] in students[data[i][j] - 1][1:]:
                    count += 1

        answer += score[count]

print(answer)