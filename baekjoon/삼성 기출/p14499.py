dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
turn_change = [[0], [3,1,0,5,4,2], [2,1,5,0,4,3], [4,0,2,3,5,1], [1,5,2,3,0,4]]

N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for i in range(N)]
command = list(map(int, input().split()))
dice = [0] * 6

def turn(d):
    tmp = [dice[i] for i in turn_change[d]]
    dice[:] = tmp[:]

for i in command:
    x += dx[i]
    y += dy[i]
    if x<0 or x>=N or y<0 or y>=M:
        x -= dx[i]
        y -= dy[i]
        continue
    turn(i)
    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0
    print(dice[0])