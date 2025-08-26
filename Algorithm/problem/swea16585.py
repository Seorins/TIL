def win(player1, player2):
    i1, v1 = player1
    i2, v2 = player2

    if v1 == v2 :
        if i1 > i2: return player2
        else : return player1

    if v1 == 1 and v2 == 2 : return player2
    if v1 == 2 and v2 == 1 : return player1

    if v1 == 2 and v2 == 3 : return player2
    if v1 == 3 and v2 == 2 : return player1

    if v1 == 3 and v2 == 1 : return player2
    if v1 == 1 and v2 == 3 : return player1


def divide_and_conquer():
    
    middle = N//2

    

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

