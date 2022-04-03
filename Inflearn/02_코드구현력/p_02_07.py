'''
7. 소수(에라토스테네스 체)
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램
''' 

import math

n = int(input())
cnt = 0

for i in range(2,n+1):
    is_prime = True
    for j in range(2, int(math.sqrt(i)+1)):
        if i%j == 0:
            is_prime = False
            break
    if is_prime:
        cnt += 1

print(cnt)
