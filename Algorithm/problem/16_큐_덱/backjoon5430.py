# R(순서 뒤집기) D(첫 번째 수 버리기)
# 비어 있을 때 D 사용하면 안됨

from collections import deque

T = int(input())

for _ in range(1, T+1):
    p = input()
    n = int(input()) # 배열 길이
    s = input().strip('[]')
    lst = list(map(int, s.split(','))) # 배열

    result = lst

    for i in p:
        if i == 'R':
            result.reverse()
        
        elif i == 'D':
            if result == []:
                print('error')
                break
            result.pop(0)

         