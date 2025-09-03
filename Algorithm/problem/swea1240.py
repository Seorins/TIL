import sys
sys.stdin = open("input.txt", "r")

T = int(input())
code_table = {
    "0001101" : 0, 
    "0011001" : 1,
    "0010011" : 2, 
    "0111101" : 3, 
    "0100011" : 4, 
    "0110001" : 5, 
    "0101111" : 6, 
    "0111011" : 7, 
    "0110111" : 8, 
    "0001011" : 9
}

def find_code():
    total = 0
    for i in range(N):
        for j in range(M-1, 55, -1):
            if matrix[i][j] == "1":
                code = matrix[i][j-55:j+1]

    for c in range(0, len(code), 7):
        if code[c:c+7] in code_table.keys():
            total += code_table[code[c:c+7]]
                
    return total 

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]

    result = find_code()

    print(f"#{tc} {result}")
