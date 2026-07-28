def insert(heap, v):
    heap.append(v)
    i = len(heap) - 1
    while i > 1 and heap[i] < heap[i // 2]:  
        heap[i], heap[i // 2] = heap[i // 2], heap[i]
        i //= 2

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0] 
    for num in arr:
        insert(heap, num)

    i = N
    sum = 0
    while i > 0:
        i //= 2
        sum += heap[i]

    print(f"#{tc} {sum}")
