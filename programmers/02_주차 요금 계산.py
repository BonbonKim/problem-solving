import math

def solution(fees, records):
    base_time, base_fee = fees[0], fees[1]
    ex_time, ex_fee = fees[2], fees[3]
    answer = list()
    cars = []

    for r in records:
        cars.append(r.split()[1])
    cars = list(set(cars))
    cars.sort()

    cars_dict = {x:[] for x in cars}
    for i in records:
        cars_dict[i.split()[1]] += [i.split()[0]]

    for i in cars_dict:
        if len(cars_dict[i]) % 2 != 0:
            cars_dict[i] += ['23:59']

    for i in cars_dict:
        time = 0
        for j in range(len(cars_dict[i])//2):
            sh, sm = map(int, cars_dict[i][2*j].split(':'))
            eh, em = map(int, cars_dict[i][2*j+1].split(':'))
            time += (eh-sh)*60 + (em-sm) # 기본 시간 180분

        fee = base_fee
        if time > base_time:
            fee += math.ceil((time-base_time)/ex_time) * ex_fee
        answer.append(fee)

    return answer