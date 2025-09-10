import sys
sys.stdin = open("input.txt", 'r')

def quicksort(A, l, r):

    if l < r : 
        p = partition(A, l, r)
        quicksort(A, l, p-1)
        quicksort(A, p+1, r)

def partition(A, l, r):
    p = A[l]

    i = l
    j = r

    while i <= j :
        while i <= j and A[i] <= p :
            i += 1

        while i <= j and A[j] >= p :
            j -= 1

        if i < j :
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]

    return j


number = list(map(int, input().split()))

quicksort(number, 0, len(number)-1)

print(number[500000])