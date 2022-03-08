from itertools import combinations
from copy import deepcopy
from collections import deque, Counter

def bfs(start, walls, board):
    maps = deepcopy(board)
    for x, y in walls:
        maps[x][y] = 1

    queue = deque(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or yy < 0 or xx >= n or yy >= m:
                continue
            if maps[xx][yy] == 0:
                maps[xx][yy] = 2
                queue.append((xx, yy))

    maps = sum(maps, [])  # 2d list -> 1d list
    return Counter(maps)[0]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []
walls = [] # 벽 가능 좌표
viruses = [] # 바이러스 좌표

n, m = map(int, input().split())
for _ in range(n):
    board.append(list(map(int, input().split())))

for x in range(n):
    for y in range(m):
        if board[x][y] == 0:
            walls.append((x, y))
        if board[x][y] == 2:
            viruses.append([x, y])

survive = 0
for i in list(combinations(walls, 3)):
    survive = max(survive, bfs(viruses, i, board))
print(survive)