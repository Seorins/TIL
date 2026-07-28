# [의상의 이름, 의상의 종류]
# 그럼 의상의 종류를 기준으로 몇 개가 있는지 파악
def solution(clothes):
    cloth_hash = {}
    
    # 의상의 종류를 기준으로 개수 저장
    for name, kind in clothes:
        cloth_hash[kind] = cloth_hash.get(kind, 0) + 1
    
    # 각 옷마다의 가능한 경우를 누적해서 곱하면 됨 
    combinations = 1
    
    for cnt in cloth_hash.values():
        combinations *= cnt + 1
    
    # 하지만 아예 아무것도 안 입는 경우가 하나 있으므로 빼줘야 함
    return combinations - 1