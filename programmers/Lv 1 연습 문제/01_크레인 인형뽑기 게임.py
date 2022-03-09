def solution(board, moves):
    new_board = [[0]]
    board_len = list(range(len(board)))

    for y in board_len:
        tmp = list()
        for x in board_len[::-1]:
            if board[x][y] != 0:
                tmp.append(board[x][y])
        new_board.append(tmp)

    cnt = 0
    picked_num = list()
    for i in moves:
        if new_board[i]:
            tmp = new_board[i].pop()
            if picked_num and tmp == picked_num[-1]:
                picked_num.pop()
                cnt += 2
            else:
                picked_num.append(tmp)

    return cnt