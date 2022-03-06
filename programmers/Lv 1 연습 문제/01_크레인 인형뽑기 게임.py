def solution(board, moves):
    new_board = list([0])
    board_len = list(range(len(board)))

    for y in board_len:  # 0 1 2 3 4
        tmp = list()
        for x in board_len[::-1]: # 4 3 2 1 0
            if board[x][y] != 0:
                tmp.append(board[x][y])
        new_board.append(tmp)

    answer = 0
    picked_num = list()
    for i in moves:
        if new_board[i]:
            tmp = new_board[i].pop()
            picked_num.append(tmp)
        if len(picked_num) >= 2 and picked_num[-2] == picked_num[-1]:
            answer += 2
            picked_num = picked_num[:-2]

    return answer
