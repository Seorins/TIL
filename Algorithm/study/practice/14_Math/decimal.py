# 10진수를 2진수로 변환
def decimal_to_binary(n):
    binary_number = "" 

    # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
    while n > 0:
        remain = n % 2
        binary_number = binary_number + remain
        n = n //2

    return binary_number

# 10진수를 16진수로 변환
def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEF"
    hexadecimal_number = ""

    if n == 0:
        return 0
    
    # 0보다 클 때까지 16으로 나누면서 나머지를 정답에 추가
    while n > 0 :
        remain = n % 16
        # 10 ~ 15를 A ~ B 로 변환 
        hexadecimal_number = hex_digits[remain] + hexadecimal_number
        n = n // 16
    return hexadecimal_number

print(decimal_to_hexadecimal(17))
print(decimal_to_hexadecimal(31))

# 내장 함수가 있기는 하다 (직접 구현하는 방법을 연산하자)
print(bin(5))
print(hex(31))


# 2진수를 10진수로 변환
def binary_to_decimal(binary_str):
    decimal_number = 0
    pow = 0

    for digit in reserved(binary_str):
        if digit == '1':
            decimal_number += 2 ** pow
        pow += 1

    return decimal_number

print(binary_to_decimal("11101"))



print("-----------------------------------")


decimal = 149

result = []

# 2로 나눈 몫이 2보다 작아질 때까지 게속 나눈다
# 나머지를 거꾸로 읽으면 이진수 완성

while decimal != 0 :
    result.append(decimal % 2)
    # 다음에 2로 나눌 숫자는 2로 나눈 몫을 나누게 될 것
    decimal = decimal // 2
     
result.reverse()
print(result)

# 비트연산자

def bit_print(dec):
    # 2진수 결과 문자열
    output = "" 

    # i는 왼쪽으로 시프트한 횟수(2진수의 자리수)
    for i in range(7, -1, -1):
        if dec & (1 << i):
            ouput += "1"
        else : 
            ouput += "0"
    
    print(output)

bit_print(149)