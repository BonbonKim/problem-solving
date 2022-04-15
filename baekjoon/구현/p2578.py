r_lines = []                    # 가로
c_lines = [[], [], [], [], []]  # 세로
x_lines = [[], []]              # 대각선
cnt = 0                         # 빙고 수

board = [list(map(int, input().split())) for _ in range(5)]
nums = []
for _ in range(5):
    nums += list(map(int, input().split()))

for b in board:
    r_lines.append(b)
    for i in range(5):
        c_lines[i].append(b[i])
for i in range(5):
    x_lines[0].append(board[i][i])
    x_lines[1].append(board[i][4 - i])

for n in range(len(nums)):
    for lines in [r_lines, c_lines, x_lines]:
        for i in range(len(lines)):
            if nums[n] in lines[i]:
                lines[i].remove(nums[n])
            if not lines[i]:
                cnt += 1
                lines[i].append(-1)

        if cnt == 3:
            print(n + 1)
            exit()