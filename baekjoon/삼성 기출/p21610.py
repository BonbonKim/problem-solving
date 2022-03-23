dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
turn = [list(map(int, input().split())) for _ in range(m)]
cloud = [[n-1,0], [n-1,1], [n-2,0], [n-2,1]]

for d, s in turn:
    check = [[0] * n for _ in range(n)]
    for i in range(len(cloud)):
        x, y = cloud[i]
        x, y = x+(dx[d]*s), y+(dy[d]*s)
        while x<0 or x>=n:
            x = n+x if x<0 else x-n
        while y<0 or y>=n:
            y = n+y if y<0 else y-n
        cloud[i] = [x, y]
        board[x][y] += 1
        check[x][y] = 1
    while cloud:
        x, y = cloud.pop()
        for i in range(2, 9, 2): # 2, 4, 6, 8
            xx, yy = x+dx[i], y+dy[i]
            if xx<0 or xx>=n or yy<0 or yy>=n or board[xx][yy]<=0:
                continue
            board[x][y] += 1
    for i in range(n):
        for j in range(n):
            if check[i][j]==0 and board[i][j]>=2:
                cloud.append([i,j])
                board[i][j] -= 2

print(sum([sum(b) for b in board]))