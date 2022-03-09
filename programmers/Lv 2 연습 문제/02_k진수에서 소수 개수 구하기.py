import math

def is_prime_num(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

def convert_10_to_k(n, k):
    num = list()
    while n > 0:
        n, rest = divmod(n, k)
        num.append(rest)
    return "".join(map(str,num[::-1]))

def solution(n, k):
    num_k = convert_10_to_k(n, k)
    num_k = num_k.split("0")

    answer = 0
    for n in num_k:
        if not n: continue
        if is_prime_num(int(n)):
            answer += 1

    return answer