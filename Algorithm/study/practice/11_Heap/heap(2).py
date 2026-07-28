def enq(n):
    global last
    last += 1
    heap[last] = n

    c = last 
    p = c // 2  # 완전이진트리 자식 -> 부모 번호 연산 

    # 부모가 있고, 부모 < 자식, 키 값 교환
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

heap = [0] * 100
last = 0 # 마지막 정점 번호 

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

print(heap)
