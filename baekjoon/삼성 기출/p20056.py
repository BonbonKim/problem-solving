# 마법사 상어와 파이어볼 https://www.acmicpc.net/problem/20056

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
board = [[list() for _ in range(n)] for _ in range(n)]
fire_balls = [list(map(int, input().split())) for _ in range(m)] # r행, c열, m (질량), s(속력), d(방향)

for _ in range(k):
    while fire_balls:
        x, y, m, s, d = fire_balls.pop()
        xx = (x-1 + dx[d]*s) % n
        yy = (y-1 + dy[d]*s) % n
        board[xx][yy].append([m, s, d])

    for x in range(n):
        for y in range(n):
            cnt_fire = len(board[x][y])
            if not cnt_fire:
                continue

            if cnt_fire == 1:
                fire_balls.append([x, y]+ board[x][y].pop())

            elif cnt_fire > 1:
                sum_m, sum_s, state, = 0, 0, 0  # 홀짝
                while board[x][y]:
                    m, s, d = board[x][y].pop()
                    sum_m += m
                    sum_s += s
                    state += 1 if d % 2 else -1  # 홀수면 +1, 짝수면 -1

                if not sum_m // 5:  # 5로 나눴을 때 질량이 0이면 소멸
                    continue

                new_d = [0, 2, 4, 6] if cnt_fire == abs(state) else [1, 3, 5, 7]  # 전부 홀수이거나, 전부 짝수이면
                for dd in new_d:
                    fire_balls.append([x, y, sum_m//5, sum_s//cnt_fire, dd])

print(sum([f[2] for f in fire_balls]))