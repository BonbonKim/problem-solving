from collections import deque
import copy

dx = [0, 1, 0, -1]  # 동(0) 남(1) 서(2) 북(3) (i++ 시계 / i-- 반시계)
dy = [1, 0, -1, 0]
dice_change = [[3, 1, 0, 5, 4, 2], [1, 5, 2, 3, 0, 4], [2, 1, 5, 0, 4, 3], [4, 0, 2, 3, 5, 1]]

def turn(d):
    tmp = [dice[i] for i in dice_change[d]]
    dice[:] = tmp[:]

def count_num(x, y, num, board):
    q = deque([(x, y)])
    maps = copy.deepcopy(board)
    maps[x][y], cnt = 0, 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if xx < 0 or xx >= n or yy < 0 or yy >= m or maps[xx][yy]==0:
                continue
            if num == maps[xx][yy]:
                maps[xx][yy] = 0
                cnt += 1
                q.append((xx, yy))
    return num * cnt

if __name__ == '__main__':
    n, m, k = map(int, input().split(' '))
    board = [list(map(int, input().split())) for i in range(n)]
    dice = [1, 2, 3, 4, 5, 6]
    cur_dir, score, x, y = 0, 0, 0, 0

    for _ in range(k):
        x += dx[cur_dir]
        y += dy[cur_dir]
        if x<0 or x>=n or y<0 or y>=m:
            x -= 2*dx[cur_dir]
            y -= 2*dy[cur_dir]
            cur_dir = cur_dir+2 if cur_dir+2 <= 3 else cur_dir-2

        turn(cur_dir)  # 주사위 굴리기 (주사위 숫자 변경)
        num = board[x][y]  # 도착한 좌표에 있는 숫자
        score += count_num(x, y, num, board)

        if dice[-1] > num:
            cur_dir += 1
        if dice[-1] < num:
            cur_dir -= 1
        cur_dir = 0 if cur_dir==4 else cur_dir
        cur_dir = 3 if cur_dir==-1 else cur_dir

    print(score)