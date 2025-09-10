
def binary_search(target):
    left = 0
    right = len(A) -1
    result = 0
    
    while left <= right : 
        mid = (left + right) // 2

        if A[mid] == target:
            return True
        
        if target < A[mid]:
            if result == 1:
                return False
            
            right = mid - 1
            result = 1

        else: 
            if result == -1 :
                return False
            left = mid + 1
            result = -1

    return False

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    total = 0
    # 1. B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 확인
    # 2. B에 속한 어떤 수가 A에 들어있으면서 동시에 탐색 과정에서 양쪽 구간을 번갈아 선택하게 되는 숫자의 개수 
    
    for target in B:
        if binary_search(target):
            total += 1

    print(f"#{tc} {total}")
    