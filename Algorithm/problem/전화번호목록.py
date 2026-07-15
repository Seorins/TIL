# 폰 북 리스트를 하나씩 해시에 추가한 후 
# 한 글자씩 추가한 후에
# 그게 해시 안에 있는지 확인하기
# 리스트로 하면 다 돌아야 하는데 해시는 1번만에 찾아지기 때문에 효율적임

def solution(phone_book):
    # 1. phone_book 해시에 추가 
    phone_hash = {}
    
    for number in phone_book : 
        phone_hash[number] = 1
        
    # 2. 이제 하나씩 추가하면서 그게 해시 안에 있는지 확인하기
    for number in phone_book : 
        temp = ""
        for num in number: 
            temp += num
            if temp in phone_hash and temp != number: 
                return False
        
    return True

        
    