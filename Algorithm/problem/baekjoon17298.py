N = int(input())
n_lst = list(map(int, input().split()))

result = [-1] * N 
stack = []

# for i in range(N):
#     for j in range(i+1, N):
#         if n_lst[i] < n_lst[j]:
#             result[i] = n_lst[j]
#             break

for i in range(N):
    while stack and n_lst[stack[-1]] < n_lst[i]:
        result[stack.pop()] = n_lst[i]
    stack.append(i)
    
print(*result)