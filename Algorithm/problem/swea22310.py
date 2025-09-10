def binary_search(target):
    left = 0
    right = target

    while left <= right : 
        mid = (left + right) // 2
        num = mid * mid

        if num == target:
            return mid
        
        if target < num:
            right = mid -1 
            
        else: 
            left = mid + 1

    return 0

T = int(input())

# 배열 만들어서 하면 런타임 에러 뜸
# 그냥 바로 타겟 넣어버리기
for tc in range(1, T+1):
    x = int(input())

    result = binary_search(x)

    print(f"#{tc} {result}")