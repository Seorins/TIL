'''
S -> T 는 경우의 수가 많음

A
ABBAABABB

i) 문자열 뒤에 A추가 AA
ii) 문자열 뒤에 B추가하고 뒤집기 AB -> BA

따라서

T -> S 로 줄여가면서 확인 

i) [젤 뒤가 A일 경우] 문자열 뒤에 A 제거
ii) [젤 앞이 B일 경우] 뒤집고 문자열 뒤에 B 제거 
'''

S = input().strip()
T = input().strip()


def transform(t):

    # 길이가 같아지면 같은 문자열인지 비교
    if len(t) == len(S):
        return t == S
    
    # 마지막이 A일 경우
    if t[-1] == 'A':
        if transform(t[:-1]):
            return True
        
    # 처음이 B일 경우 
    if t[0] == 'B':
        if transform(t[1:][::-1]):
            return True
        
    return False

print(1 if transform(T) else 0)


'''
S = "A"
T = "BA"

정방향 
(B 추가 + 뒤집기)
BA

역방향 
(앞이 B → 제거 후 뒤집기)
A
'''