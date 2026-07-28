# 최대 힙으로 사용할 배열
heap = [0] * 11

# 마지막으로 넣은 원소의 위치를 기억
last = 0

# 삽입
def enq(item):
    global last
    # item을 맨 마지막 자리에 추가
    # 맨 마지막 위치 : last +  1

    last += 1
    heap[last] = item
    
    # 일단 넣어놨는데 여기가 자리가 맞는지 확인 필요
    # 최대 힙 : 부모 > 자식
    # item의 크기와 부모 노드의 크기를 비교해서 교환
    child = last 
    # 완전이진트리  부모 = 자식 / 2
    parent = child // 2

    # child 에 있는 값과 parent에 있는 값을 비교
    # 부모 노드가 존재하고 부모 노드보다 자식이 크면 자리 계속 교환

    if parent != 0 and heap[child] > heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]

        child = parent
        parent = child // 2

lst = [6, 5, 4, 1, 3, 2, 9, 8, 10, 7]

for i in range(10):
    enq(lst[i])

print(heap)


# 삭제

def deq():
    global last
    #루트노드 삭제 전에 기억
    root = heap[1]

    # 마지막 위치 에 있느 ㄴ원소를 루트 자리로 떙겨옴
    heap[1] = heap[last]

    # 원소 제거 했으니 마지막 원소 위치도 -1
    last -= 1

    # 일단 루트자리에 마지막 원소 땡겨왔는데 
    # 거기가 자리가 맞는지 확인
    # 부모 > 자식 

    # 완전이진트리에서 부모와 지식의 인덱스
    p = 1
    c = p * 2 # 왼쪽 자식

    # 자식이 두명있으면 그중에 큰 자식과 비교해서 
    # 부모와 자리 교환

    while c <= last : 
        # c+1 : 오른쪽 자식 번호
        # 이 오른쪽 자식이 존재하는가 
        if c + 1 <= last and heap[c] < heap[c+1] :
            # 그렇다면 비교 자식은 오른쪽으로
            c = c + 1

        
        # 자식이 부모보다 큰지 확인하고 교환
        if heap[p] < heap[c]: 
            heap[p], heap[c] = heap[p], heap[c]
            p = c # 자식이 새로운 부모
            c = c * 2 # 새로운 부모 기준 왼쪽 자식 
        else: 
            # 부모가 자식보다 크녀 맞는 자리, 자리 바꾸기 중단
            break

    # 처음에 기억했던 삭제 삭제 루트 리턴
    return root 
