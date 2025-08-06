# 2차원 배열 만들기

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)


N = int(input())
arr1 = [list(map(int, input())) for _ in range(N)]
print(arr1)


arr2 = [[0]*4 for _ in range(3)]
print(arr2)

