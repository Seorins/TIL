T = int(input())

for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()

    c_list = []
    for num in carrot:
        if not c_list or num != c_list[-1][0]:
            c_list.append([num])
        else:
            c_list[-1].append(num)

    
    c_group = len(c_list)
    result = float('inf')

    if c_list < 3:
        result = -1

    min_num = float('inf')
    for l in range(1, c_group):
        for m in range(1, c_group):
            for s in range(1, c_group):
                if l + m + s == c_group:
                    result = min(result, min(max(c_list[0:l], c_list[l:l+m], c_list[l+m:l+m+s]) - min(c_list[0:l], c_list[l:l+m], c_list[l+m:l+m+s])))

    
    print(f"#{tc} {result}")
        
