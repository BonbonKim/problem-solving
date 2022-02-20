'''
6. 자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고,
그 합이 최대인 자연수를 출력하는 프로그램
'''

def sum_digit(x):
    x = str(x)
    ans = 0
    for i in range(len(x)):
        ans += int(x[i])
    return ans


max_num = 0
save_num = -1
len_num = int(input())
num_list = list(map(int,input().split()))

for i in range(len_num-1, -1, -1):
    cur_num = sum_digit(num_list[i])
    if max_num <= cur_num:
        max_num = cur_num
        save_num = i

print(num_list[save_num])


