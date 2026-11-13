def solution(bandage, health, attacks):
    now = 0
    cur_health = health
    
    for attack_time, damage in attacks:
        # 회복 가능 시간
        heal_time = attack_time - now - 1
        
        # 기본 회복
        heal = heal_time * bandage[1]
        
        # 추가 회복
        heal += (heal_time // bandage[0]) * bandage[2]
        
        # 체력 회복
        cur_health = min(health, cur_health + heal)
        
        # 피해 
        cur_health -= damage
        
        if cur_health <= 0:
            return -1
        
        now = attack_time
    
    return cur_health