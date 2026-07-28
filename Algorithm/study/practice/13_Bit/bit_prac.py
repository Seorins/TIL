bit = "00000010001101"

# 이진수를 7칸씩 쪼개서 십진수로 만들기
N = len(bit)

# 길이가 14니까 
# 0번 ~ 6번 잘라서 빠꾸고 
# 7번 ~ 13번 잘라서 바꾸고
for i in range(0, N, 7):
    # i번 비트에서 7번 잘라서 십진수로 만들고 출력
    ith_bit = bit[i:i+7]
    print(ith_bit)
    # 십진수로 바꾸기 
    decimal = 0
    pow = 0

    for i in range(0, len(ith_bit), -1):
        if i != 0 : 
            decimal += 2**int(ith_bit[pow])
        
        pow += 1

    print(decimal)

    





