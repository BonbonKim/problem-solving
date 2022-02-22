'''
7. 소수(에라토스테네스 체)
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램
''' 

import time

start_time = time.time()
num = int(input())

prime_num_list = [0] * (num+1)
prime_cnt = 0

for i in range(2, num+1):
    if prime_num_list[i] == 0:
        prime_cnt += 1
        for j in range(i, num+1, i):
            prime_num_list[j] += 1

print(prime_cnt)

end_time = time.time()
# print("time", end_time-start_time)