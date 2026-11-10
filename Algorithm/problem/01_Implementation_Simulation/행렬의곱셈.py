def solution(arr1, arr2):
    result = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for idx, val in enumerate(arr1):
        for idx2 in range(len(arr2[0])): 
            for i, v in enumerate(val):
                result[idx][idx2] += v * arr2[i][idx2]
                
    return result