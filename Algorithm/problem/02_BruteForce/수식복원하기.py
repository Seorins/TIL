# 해당 진법이 가능한지
def is_valid(num, base):
    return all(int(n) < base for n in num)

# 10진법 -> 진법
def from_decimal(num, base):
    if num == 0:
        return "0"
    
    total = ""
    
    while num > 0:
        remainder = num % base
        total = str(remainder) + total
        num //= base
        
    return total
    
# 진법 -> 10진법
def to_decimal(num, base):
    total = 0
    
    for n in num:
        total = (total * base) + int(n)
        
    return total
    
def solution(expressions):
    # 2~9진법
    bases = list(range(2, 10))
    
    for expression in expressions:
        a, oper, b, eq, c = expression.split(" ")
        
        valid_bases = []
        
        for base in bases:
            # 진법 유효성 검사
            if not is_valid(a, base) or not is_valid(b, base):
                continue
                
            if c == "X":
                valid_bases.append(base)
                continue
                
            if not is_valid(c, base):
                continue
            
            # 10진법 변환
            a_num = to_decimal(a, base)
            b_num = to_decimal(b, base)
            c_num = to_decimal(c, base)
            
            if oper == "+":
                result = a_num + b_num
                
            else: 
                result = a_num - b_num
                
            if result == c_num:
                valid_bases.append(base)
        
        bases = valid_bases
     
    
    answer = []

    # X일 경우 확인
    for expression in expressions:
        a, oper, b, eq, c = expression.split(" ")
        
        if c != 'X':
            continue
        
        base_list = []
        
        for base in bases:
            if not is_valid(a, base) or not is_valid(b, base):
                continue
                
            a_num = to_decimal(a, base)
            b_num = to_decimal(b, base)

            if oper == "+":
                result = a_num + b_num

            else: 
                result = a_num - b_num
                
            result = from_decimal(result, base)
            base_list.append(result)
            
        if base_list and len(set(base_list)) == 1:
            c = base_list[0]
            
        else:
            c = "?"
            
        answer.append(f"{a} {oper} {b} = {c}")
    
    return answer
        