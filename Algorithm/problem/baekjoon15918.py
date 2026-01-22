# 랭퍼든 수열 = 길이 2n의 수열

'''
1. 1이상 n 이하의 자연수가 각각 두 개씩
2. 두 개의 1 사이에는 정확히 1개의 수가 있음
3. 두 개의 2 사이에는 정확히 2개의 수가 있음 
... 두 개의 n ...

n이 주어졌을 때 2n의 랭퍼드 수열의 개수
x번째 수와 y번째 수는 같음(1부터 시작)
'''

def count_num(n, x, y):
    # 존재 조건
    if n % 4 not in (0, 3):
        return 0

    length = 2 * n
    x -= 1  
    y -= 1

    k = abs(y - x) - 1
    if not (1 <= k <= n):
        return 0

    seq = [-1] * length
    seq[x] = seq[y] = k

    used = [False] * (n + 1)
    used[k] = True

    def find():
        if all(used[1:]):
            return 1

        for num in range(n, 0, -1):
            if not used[num]:
                break

        count_num = 0
        for i in range(length - num - 1):
            j = i + num + 1
            if seq[i] == -1 and seq[j] == -1:
                seq[i] = seq[j] = num
                used[num] = True
                count_num += find()
                seq[i] = seq[j] = -1
                used[num] = False

        return count_num

    return find()


n, x, y = map(int, input().split())
print(count_num(n, x, y))
