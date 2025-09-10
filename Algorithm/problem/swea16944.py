def merge(left, right):
    result = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1

        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result

def merge_sort(li):

    if len(li) == 1:
        return li, 0
    
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    
    left_lst, left_cnt = merge_sort(left)
    right_lst, right_cnt = merge_sort(right)

    cnt = 0
    if left_lst[-1] > right_lst[-1]:
        cnt += 1

    merge_lst = merge(left_lst, right_lst)
    return merge_lst, left_cnt + right_cnt + cnt

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans, cnt = merge_sort(arr)
    
    print(f"#{tc} {ans[(len(ans) // 2)]} {cnt}")