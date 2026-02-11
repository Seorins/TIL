T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split()) # N개의 숫자, K번째 큰 수 
    numbers = input()   
    lst = []
    size = len(numbers) // 4 # 한 변에 있는 숫자 개수 
    result = []
    
    # 돌아가면서 다 자르고 저장한 후 변환하고 정렬해서 찾아내기
    for i in range(len(numbers)):
        if i > len(numbers) - size:
            num = i % size
            lst.append(numbers[i:]+numbers[:num])
            
        lst.append(numbers[i:i+size])

    
    for j in range(len(lst)):
        if len(lst[j]) == size:
            num = int(lst[j], 16)
            if  num not in result:
                result.append(num)

    result.sort(reverse=True)
    # print(result)
    print(f"#{tc} {result[K-1]}")
    

      
    