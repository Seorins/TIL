import sys
sys.stdin = open('input.txt', 'r')

def babygin(cards):
    counts = [0] * 10
    for c in cards:
        counts[c] += 1

    # tri
    for i in range(10):
        if counts[i] >= 3:
            return True

    # run
    for i in range(8):
        if counts[i] and counts[i+1] and counts[i+2]:
            return True

    return False


def dfs(turn, idx, p1, p2):
    global result

    if result : 
        return
    
    if idx == 12:
        return
    
    card = numbers[idx]

    if turn == 0:
        new_p1 = p1 + [card]
        if len(new_p1) >= 3 and babygin(new_p1):
            result = 1
            return
        dfs(1, idx + 1, new_p1, p2)

    else : 
        new_p2 = p2 + [card]
        if len(new_p2) >= 3 and babygin(new_p2):
            result = 2
            return
        dfs(0, idx + 1, p1, new_p2)

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    result = 0
    dfs(0, 0, [], [])

    print(f"#{tc} {result}")
