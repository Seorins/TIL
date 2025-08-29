'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(T):
    if T > 0 : 
        print(T, end= ' ')
        pre_order(left[T])
        pre_order(right[T])

def in_order(T):
    if T > 0 : 
        in_order(left[T])
        print(T, end= ' ')
        in_order(right[T])

def post_order(T):
    if T > 0 : 
        post_order(left[T])
        post_order(right[T])
        print(T, end= ' ')


V = int(input())
E = V - 1
arr = list(map(int, input().split()))

left = [0] * (V + 1) # 부모 번호를 인덱스로 자식 번호 저장
right = [0] * (V + 1) 
par = [0] * (V + 1) # 자식 번호를 인덱스로 부모 번호 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p

    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

root = 1
for i in range(1, V+1):
    if par[i] == 0 : #부모 노드가 없는 경우
        root = i
        break

pre_order(root)
print()
in_order(root)
print()
post_order(root)