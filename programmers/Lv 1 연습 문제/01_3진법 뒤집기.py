import math

def solution(n):
    digit = ''
    while n>0:
        n, r = divmod(n, 3)
        digit += str(r)
    digit = digit[::-1]
    answer = [int(digit[i]) * int(math.pow(3,i)) for i in range(len(digit))]

    return sum(answer)