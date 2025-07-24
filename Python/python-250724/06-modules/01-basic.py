# import 문 사용
import math

print(math.pi) # 3.141592653589793
print(math.sqrt(4)) # 2.0

# from 절 사용
from math import pi, sqrt

print(pi) # 3.141592653589793
print(sqrt(4)) # 2.0


# from 사용 시 사용자가 선언한 변수와 겹치면 동작이 제대로 안 이루어질 수 있음
pi = "pipi"

print(pi) # pi
