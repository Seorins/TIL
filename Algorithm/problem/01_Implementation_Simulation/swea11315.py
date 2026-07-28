def check(arr, N):
    di = [0, 1, 1, -1]
    dj = [1, 0, 1, 1]
 
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4): 
                    for k in range(5):
                        nx = i + di[d] * k
                        ny = j + dj[d] * k
                        # 범위 벗어나면 중단
                        if not (0 <= nx < N and 0 <= ny < N):
                            break
                        # 돌이 아니면 중단
                        if arr[nx][ny] != 'o':
                            break
                    else:
                        # break 없이 5칸 연속으로 o면 성공
                        return "YES"
    return "NO"

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
   
    print(f"#{tc} {check(arr, N)}")