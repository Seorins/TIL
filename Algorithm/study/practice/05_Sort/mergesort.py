
def merge(left, right):
    # 두 리스트를 병합한 결과 리스트
    result = [0] * (len(left) + len(right))
    l = r = 0 # 인덱스

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l] # result에 더 작은 걸 삽입
            l += 1

        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 데이터들을 모두 result에 추가 
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 오른쪽 리스트에 남은 데이터들을 모두 result에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result

# 1. 분할
# 2. 정복 & 병합(정렬)
def merge_sort(li): 
    
    if (len(li)) == 1:
        return li
    
    # 절반씩 분할
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    
    left_lst = merge_sort(left)
    right_lst = merge_sort(right)

    # 합치는 함수까지 구현해서 합쳐주면 됨 
    merge_lst = merge(left_lst, right_lst)
    return merge_lst

arr = [69, 10, 30, 2, 16, 8, 31, 22]

sorted_arr = merge_sort(arr)
print(sorted_arr)