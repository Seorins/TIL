def KFC(x):
    # 약 1000번 제한

    if x == 3 : # 종료조건(기저조건 - base case) : 3 스택과 유사한 구조
        return 
    
    print(x, end=" ")
    KFC(x+1)
    print(x, end=" ")

KFC(0)
print("끝")