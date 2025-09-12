'''
격자 판에는 0~9 사이의 숫자
임의의 위치에서 시작해서 동서남북 네 방향으로 총 6번 움직임 
이 글자를 이어 붙이면 7자리 수가 됨
격자판을 벗어나면 안되고 갔던 곳 다시 가도 됨

만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램 

그럼 다 가면서 7자리 수 되면 끝내기 
set으로 관리 해도 되나 ? 그럼 안에 어떤 형식으로 넣을지 (불변)
'''

def dfs(x, y, cnt, s):
    global result # 굳이 global 안 해줘도 됨 
 
    if cnt == 7:
        result.add(s) # 함수호출로 접근할 때는 안 해줘도 됨 / 단 + 연산은 안됨(지역변수 초기화가 안돼서)
        return
             
    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx, ny = x + di, y + dj
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, cnt + 1, s + graph[nx][ny])
 
T = int(input())
 
for tc in range(1, T+1):
    graph = [list(input().split()) for _ in range(4)]
    result = set()
     
    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, graph[i][j])
 
    print(f"#{tc} {len(result)}")

