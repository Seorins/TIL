import requests
from pprint import pprint

url = "https://fakestoreapi.com/carts"

data = requests.get(url) # 조회
print(data) # 200 정상 
# 404 : not found (서버는 제대로 적고 데이터 종류에서 잘못 적었을 때 -> carts)

data_content = requests.get(url).json()
pprint(data_content)

