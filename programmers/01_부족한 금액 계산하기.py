def solution(price, money, count):
    fee = sum([price*c for c in range(1, count+1)])
    answer = fee-money if fee-money > 0 else 0

    return answer
