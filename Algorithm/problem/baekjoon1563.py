'''
[출석, 지각, 결석]

개근상 X = 지각을 두 번 이상 / 결석 세 번 연속

한 학기가 4일이고, O를 출석, L을 지각, A를 결석이라고 했을 때

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA 
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO 
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA 
LAOO LAOA LAAO
총 43가지이다.

'''

N = int(input()) # 한 학기 일수 

whole = N ** 3 # 전체 

# 안 되는 날 
# i) 지각 두 번 이상 => 전체 - 지각 0/1 일경우 
# 0 => 1
# 1 => N

# ii) 결석 세 번 연속 
# N - 3 + 1

print(whole - (1+N) - (N-3+1))


