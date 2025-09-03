# 힙을 저장할 배열
# 편의상 1번 인덱스부터 사용하기 위해 맨 앞에 None 추가
heap = [None]  

# 삽입 연산 (Heapify Up)
def push(x):
    heap.append(x)              # 1) 마지막 위치에 새로운 값 추가
    i = len(heap) - 1           # 현재 삽입된 위치 인덱스

    # 2) 부모와 비교해서 "힙 성질"을 만족할 때까지 위로 올림
    while i > 1 and heap[i//2] < heap[i]:  
        heap[i//2], heap[i] = heap[i], heap[i//2]  # 부모와 자리 바꾸기
        i //= 2   # 부모 위치로 인덱스 갱신

# 삭제 연산 (Heapify Down)
def pop():
    if len(heap) == 1:          # 힙이 비어 있으면 None 반환
        return None

    top = heap[1]               # 루트(최대값) 저장
    heap[1] = heap[-1]          # 마지막 원소를 루트로 이동
    heap.pop()                  # 마지막 원소 제거

    # 2) 루트에서 아래로 내려가며 "힙 성질" 회복
    i = 1
    while True:
        left, right = i*2, i*2+1
        largest = i

        # 왼쪽 자식이 존재하고, 부모보다 크면 largest 갱신
        if left < len(heap) and heap[left] > heap[largest]:
            largest = left
        # 오른쪽 자식도 검사
        if right < len(heap) and heap[right] > heap[largest]:
            largest = right

        if largest == i:        # 자식 둘 다 부모보다 작으면 종료
            break

        # 부모와 더 큰 자식 교환
        heap[i], heap[largest] = heap[largest], heap[i]
        i = largest             # 인덱스를 자식 위치로 옮김

    return top

# -------------------------------
# 사용 예시
# -------------------------------
push(10)
push(5)
push(20)
push(15)

print(pop())  # 20 (최대 힙이므로 최댓값이 삭제됨)
print(pop())  # 15
