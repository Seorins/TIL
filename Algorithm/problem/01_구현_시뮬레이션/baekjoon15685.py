'''
드래곤 커브 -> 세가지 속성
1. 시작점
2. 시작 방향
3. 세대

0세대 
길이가 1인 선분

1세대 
0세대 드래곤 커브를 끝 점 기준으로 시계 방향 90도 회전시킨 다음
0세대 드래곤 커브의 끝점에 붙임

K세대
K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 
그것을 끝 점에 붙인 것

100*100 드래곤 커브 N개 

0: x좌표 증가 방향 (오른쪽)
1: y좌표 감소 방향 (위)
2: x좌표 감소 방향 (왼쪽)
3: y좌표 증가 방향 (아래)
'''

import sys
input = sys.stdin.readline

N = int(input())

# 오 위 왼 아래
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

board = [[0] * 101 for _ in range(101)]

for _ in range(N):
    # x, y 시작점 / d 시작 방향 / g 세대 
    x, y, d, g = map(int, input().split())

    directions = [d]

    for _ in range(g):
        for i in range(len(directions) - 1, -1, -1):
            directions.append((directions[i] + 1) % 4)

    board[y][x] = 1

    for dir in directions:
        x += dx[dir]
        y += dy[dir]
        board[y][x] = 1

result = 0

for y in range(100):
    for x in range(100):
        if board[y][x] and board[y][x + 1] and board[y + 1][x] and board[y + 1][x + 1]:
            result += 1

print(result)