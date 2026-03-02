'''
- N개의 원자 / (x, y) 좌표에서 시작
- 상, 하, 좌, 우 1초에 1만큼 이동.
- 두 원자가 같은 위치에서 만나면 에너지를 방출하고 소멸
-> 모든 충돌에서 방출된 에너지의 총합
'''

def calculate():
    if not collision:
        return 0

    collision.sort(reverse=True)

    used = set()
    result = 0

    dist, p, q = collision.pop()
    result += lst[p][3] + lst[q][3]
    used.add(p)
    used.add(q)

    while collision:
        d, x, y = collision.pop()

        if dist == d and p == x and y not in used:
            result += lst[y][3]
            used.add(y)

        elif x not in used and y not in used:
            result += lst[x][3] + lst[y][3]
            used.add(x)
            used.add(y)
            dist, p, q = d, x, y

    return result


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort(key=lambda x: x[0])

    collision = []

    for p in range(n - 1):
        for q in range(p + 1, n):
            dx = lst[p][0] - lst[q][0]
            dy = lst[p][1] - lst[q][1]

            if dx == 0:
                if lst[p][2] == 0 and lst[q][2] == 1 and dy < 0:
                    collision.append([abs(dy), p, q])
                elif lst[p][2] == 1 and lst[q][2] == 0 and dy > 0:
                    collision.append([abs(dy), p, q])

            elif dx == dy:
                if lst[p][2] == 0 and lst[q][2] == 2 and dy < 0:
                    collision.append([abs(dx) + abs(dy), p, q])
                elif lst[p][2] == 3 and lst[q][2] == 1 and dy < 0:
                    collision.append([abs(dx) + abs(dy), p, q])

            elif dx * -1 == dy:
                if lst[p][2] == 3 and lst[q][2] == 0 and dy > 0:
                    collision.append([abs(dx) + abs(dy), p, q])
                elif lst[p][2] == 1 and lst[q][2] == 2 and dy > 0:
                    collision.append([abs(dx) + abs(dy), p, q])

            elif dy == 0:
                if lst[p][2] == 3 and lst[q][2] == 2:
                    collision.append([abs(dx), p, q])

    print(f"#{tc} {calculate()}")