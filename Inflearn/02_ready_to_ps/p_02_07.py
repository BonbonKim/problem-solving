'''
7. 소수(에라토스테네스 체)
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램
-> 시간 초과, 다시 풀어보기
''' 

import time

start_time = time.time()
num = int(input())
prime_num_list = list()

for i in range(2, num + 1):
    is_prime_num = True
    for j in range(2, i):
        if i % j == 0:
            is_prime_num = False
            break
    if is_prime_num:
        prime_num_list.append(i)

print(len(prime_num_list))
end_time = time.time()
# print("time", end_time-start_time)