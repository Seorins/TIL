# try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print(result)
finally:
    print("프로그램을 종료합니다.")


try:
    result = int(input("숫자를 입력하세요 : "))
except ValueError:
    print("숫자를 입력해주세요")


    
