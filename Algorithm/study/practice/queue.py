class Queue :
    def __init__(self):
        self.queue = []

    # 삽입 (enqueue)
    def enqueue(self, item):
        self.queue.append(item) # 리스트 뒤에 추가

    # 삭제 (dequeue)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0) # 리스트 맨 앞에서 제거

    # front 원소 확인
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    # 큐가 비었는지 확인
    def is_empty(self):
        return len(self.queue) == 0
    
    # 큐 크기 확인
    def size(self):
        return len(self.queue)
    
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print(q.dequeue())  # A
print(q.peek())     # B
print(q.dequeue())  # B
print(q.dequeue())  # C
print(q.dequeue())  # None (비어있음)


# 선형 큐 
class LinearQueue :
    def __init__(self, max_size):
        self.queue = [None] + max_size
        self.max_size = max_size 
        self.front = -1 # 아직 출발 안 함
        self.rear = -1

    def is_empty(self):
        return self.front == self.rear
    
    # 끝의 인덱스가 마지막까지 감
    def is_full(self):
        return self.rear == self.max_size -1 
    
    def enqueue(self, item):
        if self.is_full():
            print("큐가 가득 참")
        self.rear += 1
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_full():
            print("큐가 비었음")
            return None
        self.front += 1
        return self.queue[self.front]


# 원형 큐
class CircularQueue:
    def __init__(self, max_size):
        self.max_size = [None] * max_size
        self.max_size = max_size
        self.front = 0 # 원형은 front 자리를 비워두기 때문에 0을 함 (삭제 직전 자리)
        self.rear = 0 

    
