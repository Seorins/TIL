N = int(input()) # 멀티탭 구멍 개수 
K = int(input()) # 전기 용품 총 사용 횟수 

names = list(map(int, input().split())) 

plugs = [] # 콘센트 관리 

for i in range(K):
    # 1) 이미 동일한 게 꽂혀있으면 패스
    if names[i] in plugs:
        pass
    
    # 2) 만약 콘센트가 비어있다면 그냥 추가 
    elif len(plugs) < N :
        plugs.append(names[i])
        
    # 3) 플러그가 다 찼을 경우 
    # 가정 : 뒤에 남은 수가 가장 적은 물건을 교체시키기 
    