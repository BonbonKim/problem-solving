'''
8. 뒤집은 소수
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램
'''

def reverse_num(x):
    x = list(str(x))
    x = x[::-1]
    return int("".join(x))

def is_prime(x):
    is_prime_num = True
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                is_prime_num = False
                break
    else:
        is_prime_num = False
    return is_prime_num


num_of_digit = int(input())
num_list = list(map(int, input().split()))
results = list()

for i in num_list:
    cur_num = reverse_num(i)
    if is_prime(cur_num):
        results.append(cur_num)

print(" ".join(map(str, results)))
