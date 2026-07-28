def print_subset(bit):
    for i in range(4):
        if bit[i]:
            print(arr[i], end=" ")
    print(bit)


arr = [7, 5, 8, 1]

bit = [0, 0, 0, 0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l

                print_subset(bit)


print('-------------------------------------------------------------')

arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=", ")
    print(f" : {i:06b}")
print()


print('-------------------------------------------------------------')