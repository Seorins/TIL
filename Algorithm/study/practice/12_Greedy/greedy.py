# 규칙 : 큰 동전부터 빼주자 
coin_list = [100, 50, 500, 10]
target = 1730
result = 0


# Greedy 문제의 단골 손님
# 정렬 연습 : 튜플이라면 ? 인스턴스 리스트 ? 역순이라면 ? 
# 예) 길이가 우선 정렬, 같은 길이는 사전 순으로 정렬

coin_list.sort(reverse=True) # 큰 동전부터 사용
print(coin_list)

for coin in coin_list:
    possible_cnt = target // coin # 현재 동전으로 가능한 최대 수 
    result += possible_cnt # 정답에 더해준다
    target -= coin * possible_cnt # 쓴 만큼 금액을 빼준다

print(result)
    # 현재 동전으로 가능한 최대 수 
    # 정답에 더해준다
    # 급액을 빼준다

