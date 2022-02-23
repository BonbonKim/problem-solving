'''
2. 휴가 (DFS)
오늘부터 N+1일째 되는 날 휴가를 가기 위해서, 남은 N일 동안 최대한 많은 상담을 해서 휴가비를 넉넉히 만들어 휴가를 떠나려 한다.
각각의 상담은 상담을 완료하는데 걸리는 날수 T와 상담을 했을 때 받을 수 있는 금액 P로 이루어져 있다.

현수가 휴가를 가기 위해 얻을 수 있는 최대 수익을 구하는 프로그램
'''

def DFS(i, spend_time, acc_cash):
    global total_cash
    if i == total_day:
        if total_cash < acc_cash:
            total_cash = acc_cash
    else:
        add_time = reserv_table[i][0]
        add_cash = reserv_table[i][1]
        # 상담 예약 가능
        if spend_time == 0 and i+add_time <= total_day:
            DFS(i+1, add_time-1, acc_cash+add_cash)  # 상담 잡음
            DFS(i+1, 0, acc_cash)  # 상담 안잡음
        # 상담 예약 불가능
        else:
            DFS(i+1, spend_time-1, acc_cash) # 상담 안잡음

if __name__ == '__main__':
    total_day = int(input())
    reserv_table = list()

    for i in range(total_day):
        reserv_table.append(tuple(map(int, input().split())))

    total_cash = 0
    DFS(0, 0, 0)
    print(total_cash)