'''
8. 뒤집은 소수
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램
'''

import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

_ = input()
nums = list(map(str, input().split()))
answer = []
for n in nums:
    n = int(n[::-1])
    if is_prime(n):
        answer.append(str(n))
print(' '.join(answer))
