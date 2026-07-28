N = 10
p = [0] * (N+1)


# 초기화 연산
# x 자기 자신이 대표인 집합을 만듦
def make_set(x):
    p[x] = x


# x가 속한 집합의 대표가 누구인지
def find_set(x):
    if p[x] == x :
        return x
    return find_set(p[x])


# 경로 압축 버전
# 모든 x에 대해서 find_set2(x)가 한 번씩 호출이 돼야 경로 압축이 일어남
def find_set2(x):
    if p[x] != x :
        p[x] = find_set2(p[x])

    return p[x]


# x가 속한 집합과 y가 속한 집합을 합침
def union(x, y):
    # x가 속한 집합의 대표를 구함
    king_x = find_set(x)

    # y가 속한 집합의 대표를 구함
    king_y = find_set(y)

    # 두 집합의 대표가 같으면 합칠 필요 x
    if king_x == king_y :
        return 
    
    # 더 작은 쪽 or x를 대표로
    p[king_y] = king_x

# 랭크를 사용한 집합의 높이 구별
# 랭크가 작은 집합을 랭크가 큰 집합에 합침
rank = [0] * (N+1)

def union2(x, y):
    king_X = find_set2(x)
    king_y = find_set2(y)

    # 합칠 때 두 집합의 랭크를 비교해서 더 큰 쪽을 대표로 삼겠다
    if rank[king_X] > rank[king_y]:
        p[king_y] = king_X

    else :
        p[king_X] = king_y
        # 랭크가 같은 경우 
        if rank[king_X] == rank[king_y]:
        # 위에서 y가 대표가 되었으니 y의 랭크 +1
            rank[king_y] += 1


# makeset 함수 대신 그냥 list comprehension으로 만들어도 됨