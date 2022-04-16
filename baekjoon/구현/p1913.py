dr = [0, 1, 0, -1]  # → ↓ ← ↑
dc = [1, 0, -1, 0]

n = int(input())
target = int(input())

board = [[0]*n for _ in range(n)]
answer = []

num, dd = 1, 1
r, c = int((n-1)/2), int((n-1)/2) # start
if num == target:
    answer = [r+1, c+1]
board[r][c] = num

while True:
    r, c = r+dr[3], c+dc[3]  # ↑

    if r < 0: break
    num += 1
    if not answer and num == target:
        answer = [r+1,c+1]
    board[r][c] = num

    for i in range(4):
        for j in range(dd):
            r, c = r+dr[i], c+dc[i]  # → ↓ ← ↑
            num += 1
            if not answer and num == target:
                answer = [r+1,c+1]
            board[r][c] = num
        if i in [0, 3]:
            dd += 1

for b in board:
    print(" ".join(map(str,b)))
print(" ".join(map(str,answer)))