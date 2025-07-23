# Functions

## 함수(Function)의 정의
- 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
  
### 함수를 사용하는 이유
- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
- **재사용성**이 높아지고 코드의 **가독성과 유지보수성** 향상

### 함수 호출(function call)
- 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것 
- function_name(arguments)

## 함수 구조 
- Input x (parameter) -> Docstring / function body -> Output f(x) (return value)

### 함수 정의와 호출
- 함수 정의
  - 함수 정의는 def 키워드로 시작
  - def 키워드 이후 함수 이름 작성
  - 괄호 안에 매개변수를 정의할 수 있음
  - 매개변수(parameter)는 함수에 전달되는 값

- 함수 body
  - 콜론(:) 다음에 들여쓰기 된 코드 블록
  - 함수가 실행 될 때 수행되는 코드를 정의

- Docstring 
  - 함수 body 앞에 선택적으로 작성 가능한 함수 설명서 (선택사항)

- 함수 반환 값
  - 함수는 필요한 경우 결과를 반환할 수 있음
  - return 키워드 이후에 반환할 값을 명시
  - return 문은 함수의 실행을 종료하고 결과를 호출 부분으로 반환
  - **함수 내에서 return 문에 없다면 None이 반환됨**

## TIP. 표현식 평가 순서와 print, return 차이

### 표현식 평가 순서

- 파이썬은 항상 **오른쪽을 먼저 실행**하고, 그 결과를 **왼쪽 변수에 할당**함.
  
```python
value = print(1)  # 1을 출력하고, value에는 None이 저장됨
sum = 1 + 2       # 1 + 2를 계산한 결과 3이 sum에 저장됨
```

| 구분    | print()        | return                |
| ----- | -------------- | --------------------- |
| 목적    | 값을 **출력**함     | 값을 **반환**함            |
| 반환값   | `None`         | 원하는 값을 반환함 (`return`) |
| 사용 위치 | 주로 디버깅, 결과 확인용 | 함수 결과를 저장하거나 활용할 때    |

- 함수 호출
  - 함수르 사용하기 위해서는 호출이 필요
  - 함수의 이름과 소괄호를 활용해 호출
  - 필요한 경우 인자(argument)를 전달해야 함
  - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨 

### print() 함수는 반환 값이 없음
- print() 함수는 화면에 값을 출력하기만 할 뿐 반환 값이 없음
- 파이썬에서 **반환 값이 없는 함수는 기본적으로 None을 반환**한다고 간주되기 때문
- 출력을 담당하는 함수는 결과를 반환하지 않으므로 내부적으로 아무 값도 반환하지 않는 함수와 마찬가지로 None이 나옴
- **출력과 반환은 엄연히 다른 것!**

```python
return_value = print(1)
print(return_value) #None
```

---

## 매개변수(parameter)
- 함수를 정의할 때, 함수가 받을 값을 나타내는 변수

## 인자(argument)
- 함수를 호출할 때, 실제로 전달되는 값

```python
def add_num(x, y): # x와 y는 매개변수(parameter)
  result = x + y
  return result

a = 2
b = 3

sum_result = add_num(a, b) # a와 b는 인자(argument)
print(sum_result)
```

### 다양한 인자 종류
1. 위치 인자
2. 기본 인자 값
3. 키워드 인자
4. 임의의 인자 목록
5. 임의의 키워드 인자 목록

* 인자 : 함수를 호출할 때, 실제로 전달되는 값


### 1. Positional Arguments (위치 인자)
- 함수 호출 시 인자의 위치에 따라 전달되는 인자
- 위치 인자는 함수 호출 시 반드시 값을 전달해야 함
  
```python
def greet(name, age):
  print(f'안녕하세요, {name}님! {age}살이군요.')

greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.
greet(25, 'Alice') # 안녕하세요, 25남! Alice살이시군요.
greet('Alice') #TypeError
```

### 2. Default Argument Values (기본 인자 값)
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호츨 시 인자를 전달하지 않으면, 기본 값이 매개변수에 할당됨 

```python
def greet(name, age=30):
  print(f'안녕하세요, {name}님! {age}살이군요.')

greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.
greet('Alice') # 안녕하세요, Alice님! 30살이시군요.
```

### 3. Keyword Arguments (키워드 인자)
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며 인자의 이름을 명시하여 전달
- **단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함**
  
```python
def greet(name, age):
  print(f'안녕하세요, {name}님! {age}살이군요.')

greet(name='Alice', age=25) # 안녕하세요, Alice님! 25살이시군요.
greet(age=25, name='Alice') # 안녕하세요, Alice님! 25살이시군요.

greet(age=25, 'Alice') # positional argument follows keyword argument
```

### 4. Arbitrary Argument Lists (임의의 인자 목록)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 **매개변수 앞에 '*'를 붙여 사용**
- **여러 개의 인자를 tuple로 처리**

```python
def calculate_sum(*args):
  print(args) # (1, 100, 5000, 30)
  print(type(args)) # <class 'tuple'>

caculate_sum(1, 100, 5000, 30)
```

### 5. Arbitrary Keyword Argument Lists (임의의 키워드 인자 목록)
- 정해지지 않은 개수의 키워드 인자를 처리하느 ㄴ인자
- 함수 정의 시 매개변수 앞에 '**'를 붙여 사용
- **여러 개의 인자를 dictionary로 묶어 처리**
  
```python
def print_info(**kargs):
  print(kargs) # (1, 100, 5000, 30)

print_info(name='Eve', age=30) #{'name' : 'Eve', 'age': 30}
```

### 함수 인자 권장 작성 순서
- 위치 -> 기본 -> 가변 -> 가변 키워드
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
- **단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 잇음**
- *'default'가 파라미터에 있을 경우 문자열이 들어와야 한다는 제한을 두는 것이 아니라 값이 안 들어올 경우 default라는 문자열을 대신하겠다는 의미*
- *인자 자체에서 데이터 타입을 강제할 수 없음*
--- 

## 재귀 함수
- 함수 내우벵서 자기 자신을 호출하는 함수

### 재귀 함수 예시 - 팩토리얼
- factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
- 재귀 호출은 n이 0이 될 때 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함
- 재귀 호출의 결과를 이용하여 문제를 작은 단위의 문제로 분할하고, 분활된 문제들의 결과를 조합하여 최종 결과를 도출 

```python
def factorial(n): 
  if n == 1:
    return 1
  else : 
    return n * factorial(n-1)

print(factorial(5)) # 120
```
### 재귀 함수 특징
- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

### 재귀 함수 활용 시 기억해야 할 것
- 종료 조건을 명확히 할 것
- 반복되는 호출이 종료 조건을 향하도록 할 것

* 스택 오버플로우 : 작업 공간에 일이 너무 많이 쌓여 프로그램이 멈추는 오류 (스택에도 제한이 있음)

### TIP
- 재귀 함수는 메모리 사용량이 많고 느릴 수 있음
- 종료 조건이 잘못되면 스택 오버플로우 에러가 발생할 수 있으니 주의 해야 함
- 복잡한 재귀 함수는 오히려 코드의 가독성을 저하시킬 수 있음

### 재귀 함수를 사용하는 이유
- 문제의 자연스로운 표현 
  - 복잡한 문제를 간결하고 직관적으로 표현 가능
- 코드 간결성
  - 상황에 따라 반복문보다 알고리즘 코드가 더 간결하고 명확해질 수 있음
- 수학적 문제 해결
  - 수학적 정의가 재귀적으로 표현되는 경우, 직접적인 구현 가능

---

## 내장 함수(Built-in function) 
- 파이선이 기본적으로 제공하는 함수(별도의 import 없이 바로 사용 가능)
- 내장 함수는 편리하지만, 이름이 같아도 다른 언어에서는 다르게 동작할 수 있기에 주의해야 함
- 단순히 함수를 사용하는 것에 그치지 않고, 내부 동작 원리를 이해하면 문제 해결에 더 효과적으로 활용하고 성능 저하 같은 잠재적 문제를 피할 수 있음

## 자주 사용되는 내장 함수 예시 
```python
numbers = [1, 2, 3, 4, 5]

print(numbers) # [1, 2, 3, 4, 5]
print(len(numbers)) # 5
print(max(numbers)) # 5
print(min(numbers)) # 1
print(sum(numbers)) # 15
print(sorted(numbers, reverse=True)) # [5, 4, 3, 2, 1]
```

---

## Python의 범위(Scope)
- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분

### 범위와 변수 관계 
- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)
- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수

### Scope 예시
- num은 local scope에 존재하기 때문에 global scope에서 사용할 수 없음 => 이는 변수의 **수명 주기**와 연관이 있음

* local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)
* global scope : 코드 어디서든 참조할 수 있는 공간 

### 변수 수명주기(lifecycle)
- 변수의 수명주기는 변수가 선언되는 위치가 scope에 따라 결정됨
1. built-in-scope
   - 파이썬이 실행된 이후부터 영원히 유지
2. global scope
   - 모둘이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope
   - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 이름 검색 규칙(Name Resolution)
- 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름
  1. Local scope : 지역 범위(현재 작업 중인 범위)
  2. Enclosed scope : 지역 범위 한 단계 위 범위
  3. Global scope : 최상단에 위치한 범위
  4. Built-in scope : 모든 것을 담고 있는 범위
     (정의하지 않고 사용할 수 있는 모든 것)
- **함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음**

### LEGB Rule 예시 
- sum이라는 이름을 global scope에서 사용함으로써, 기존 built-in scope에 있던 내장함수를 sum을 사용하지 못하게 됨
=> sum을 참조 시 LEGB Rule에 따라 global에서 먼저 찾기 때문

```python
print(sum)                  # <built-in function sum>
print(sum(range(3)))        # 3 → 내장 함수 sum을 사용해서 0+1+2

sum = 5                     # 이제 sum이라는 이름을 정수 5로 덮어씀

print(sum)                  # 5 (이제 sum은 함수가 아니라 int임)
print(sum(range(3)))        # TypeError: 'int' object is not callable

```

```python
x = 'G'
y = 'G'

def outer_func():
    x = 'E'
    y = 'E'

    def inner_func(y):     # 이 y는 매개변수 → local
        z = 'L'
        print(x, y, z)     # E P L

    inner_func('P')
    print(x, y)            # E E

outer_func()
print(x, y)                # G G
```

* 전역 변수는 함수를 호출해도 영향을 끼치지 않음

---

## global
- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

```python
num = 0  # 전역 변수

def increment():
    global num  # num을 전역 변수로 선언
    num += 1

print(num)      # 0
increment()
print(num)      # 1
```

### global 키워드 주의사항
- global 키워드 선언 전에 참조 불가
- 매개변수에는 global 키워드 사용 불가

---

## 함수 스타일 가이드
### 함수 이름 작성 규칙
### 기본 규칙
- 소문자와 언더스코어(_) 사용(snake_case)
- 동사로 시작하여 함수의 동작 설명
- 약어 사용 지양 

### 함수 이름 구성 요소
- 동사 + 명사
  - save_user()
- 동사 + 형용사 + 명사
  - calculate_total_price()
- get/set 접두사
  - get_username(), set_username()

### TIP
- 이름만으로 '무엇을 하는지' 명확하게 표현
- True/False를 반환한다면 is 또는 has로 시작하는 것이 좋음
- 프로젝트 전체에서 일관성으로 지키는 것이 가독성에 도움을 줌

### 단일 책임 원칙(Single Responsibility Principle)
- 모든 객체는 하나의 명확한 목적과 책임만을 가져야 함

### 함수 설계 원칙
1. 명확한 목적
   1. 함수는 한 가지 작업만 수행
   2. 함수 이름으로 목적을 명확히 표현
2. 책임 분리
   1. 데이터 검증, 처리, 저장 등을 별도 함수로 분리
   2. 각 함수는 독립적으로 동작 가능하도록 설계 
3. 유지보수성
   1. 작은 단위의 함수로 나누어 관리 
   2. 코드 수정 시 영향 범위를 최소화 

## Packing & Unpacking
### 패킹(Packing)
- 여러 개의 데이터를 하나의 컬렉션으로 모아 담는 과정
- 여러 개의 값을 하나의 튜플로 묶는 파이썬의 기본 동작
- 한 변수에 콤마로 구분된 값을 넣으면 자동으로 튜플로 처리

```python
packed_values = 1, 2, 3, 4, 5
print(packed_values) # (1, 2, 3, 4, 5)
```

### '*'를 활용한 패킹 (함수 매개변수 작성 시)
- 남는 위치 인자들을 튜플로 묶기 
- *를 붙인 매개변수가 남는 위치 인자들을 모두 모아 하나의 튜플로 만듦

### '**'를 활용한 패킹 (함수 매개변수 작성 시)
- 남는 키워드 인자들을 딕셔너리로 묶기
- **를 붙인 매개변수가 남는 키워드 인자들을 모두 모아 하나의 딕셔너리로 만듦

### print 함수의 패킹 예시
- print 함수에서 임의의 가변 인자를 작성할 수 있었던 이유
=> 인자 개수에 상관 없이 튜플 하나로 패킹 되어서 내부에서 처리
- 기본 인자 수정 가능 print('hi', end=" ")

### 언패킹(Unpacking)
- 컬렉션에 담겨있는 데이터들을 개별 요소로 펼쳐 놓는 과정
- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
- '시퀀스 언패킹(Sequence Unpacking)' 또는 '다중 할당(Multiple Assignment)'이라고 부름
  
### '*을 활용한 언패킹 (함수 인자 전달)
- 리스트나 튜플 앞에 *를 붙여 각 요소를 함수의 개별 위치 인자로 전달

### '**'을 활용한 언패킹 (딕셔너리 -> 함수 키워드 인자)
- 딕셔너리 앞에 **를 붙여 {키:값} 쌍을 키 = 값 형태의 키워드 인자로 전달

### Packing & Unpacking, * & ** 정리 
## ⭐️ * / ** 연산자 (Packing & Unpacking)

| 구분     | 상황         | `*` 연산자 설명                                  | `**` 연산자 설명                                 |
|----------|--------------|--------------------------------------------------|--------------------------------------------------|
| 패킹     | 함수 정의 시  | 여러 위치 인자를 하나의 **튜플**로 받음           | 여러 키워드 인자를 하나의 **딕셔너리**로 받음    |
| 언패킹   | 함수 호출 시  | 리스트/튜플을 개별 **위치 인자**로 전달           | 딕셔너리를 개별 **키워드 인자**로 전달           |

```python
# 패킹 예시
def func(*args, **kwargs):
    print(args)    # 튜플
    print(kwargs)  # 딕셔너리

func(1, 2, 3, a=4, b=5)

# 언패킹 예시
nums = [1, 2, 3]
options = {'a': 4, 'b': 5}

func(*nums, **options)
```

---

## 함수와 반환
### 함수의 return, 반환의 원칙
- 파이썬 함수는 언제나 단 하나의 값(객체)만 반환할 수 있음
- 여러 값을 반환하는 경우에도 하나의 튜플로 패킹하여 반환

```python
def get_user_info():
    name = 'Alice'
    age = 30
    # 콤마(,)로 여러 값을 반환 → 하나의 튜플로 반환됨
    return name, age

# 반환된 값을 user_data에 저장
user_data = get_user_info()

# 단 하나의 튜플을 반환한 것
print(user_data)  # ('Alice', 30)
```

### 파이썬 함수의 반환 핵심
1. 파이썬 함수는 오직 **하나의 값(객체)**만 return 할 수 있음
2. return a, b, c 처럼 콤마를 사용하면, 파이썬이 값들을 하나의 튜플로 자동 패킹하여 반환
3. 반환된 튜플은 각 변수에 언 패킹하여 사용할 수 있음

---

## 람다 표현식(Lamda expressions)
- 익명 함수를 만드는 데 사용되는 표현식
- 한 줄로 간단한 함수를 정의 
- **단, 람다 표현은 그 자체로 실행되지 않음**
  **=> 변수에 담거나 함수의 인자로 넣어야 쓸 수 있음** 

### 람다 표현식 구조
- lambda 키워드 
  - 람다 함수를 선언하기 위해 사용되는 키워드
- 매개변수
  - 함수에 전달되는 매개변수들
  - 여러 개의 매개변수가 있을 경우 쉼표로 구분
- 표현식
  - 함수의 실행되는 코드 블록으로, 결과 값을 반환하는 표현식으로 작성
- 표기법
  - lambda 매개변수: 표현식

### 람다 표현식 예시
- 간단한 연산이나 함수를 한 줄로 표현할 때 사용
- 함수를 매개변수로 전달하는 경우에도 유용하게 활용 
  
### lambda 표현식 활용 (with map 함수)

`map()` 함수는 반복 가능한 객체(iterable)의 요소에 함수를 적용해 새로운 이터레이터를 반환  
`lambda` 표현식은 짧은 익명 함수를 만들 때 사용

```python
numbers = [1, 2, 3, 4, 5]

# 일반 함수 정의 방식
def square(x):
    return x ** 2

# lambda 미사용 (함수 직접 정의해서 사용)
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용 (익명 함수)
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]
```