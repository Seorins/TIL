def dfs(start, word):

    if len(word) == L:
        mo_cnt = sum(1 for w in word if w in lst)
        ja_cnt = L - mo_cnt

        if mo_cnt >= 1 and ja_cnt >= 2:
            print(''.join(word))
        
        return 

    for i in range(start, C):
        dfs(i+1, word + [S[i]])


# 자리수 L 총 문자 개수 C
L, C = map(int, input().split())
S = input().split()
S.sort()

lst = ['a', 'e', 'i', 'o', 'u']

dfs(0, [])

