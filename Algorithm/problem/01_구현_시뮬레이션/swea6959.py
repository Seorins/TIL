def game(num):
    cnt = 0  
    while len(num) > 1:  
        num = str(int(num[0]) + int(num[1])) + num[2:]
        cnt += 1  
         
    # 턴 수가 홀수인지 짝수인지 확인
    if cnt % 2:
        return 'A'
    else:
        return 'B'
 
T = int(input())  

for tc in range(1, T+1):
    number = input()  

    print('#{} {}'.format(tc, game(number)))