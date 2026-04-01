import sys
import heapq

input = sys.stdin.readline

N, H, T = map(int, input().split())

heap = []
for _ in range(N):
    h = int(input())
    heapq.heappush(heap, -h)

used = 0

for _ in range(T):
    tallest = -heap[0]

    # 가장 큰 거인도 센티보다 작으면 성공
    if tallest < H:
        print("YES")
        print(used)
        break

    # 키가 1이면 더 이상 줄일 수 없음
    if tallest == 1:
        print("NO")
        print(tallest)
        break

    # 가장 큰 거인을 반으로 줄여 다시 넣기
    heapq.heappop(heap)
    heapq.heappush(heap, -(tallest // 2))
    used += 1

else:
    tallest = -heap[0]
    if tallest < H:
        print("YES")
        print(used)
    else:
        print("NO")
        print(tallest)