'''
5. 수들의 합
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+…+A[j-1]+A[j]가
M이 되는 경우의 수를 구하는 프로그램
'''

num_len, target = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.append(0)
check = 0

start = 0
end = 1
sum_n = num_list[0]

while True:
    if sum_n <= target:
        if end > num_len:
            break

        if sum_n == target:
            # print(start,end)
            check += 1
        sum_n += num_list[end]
        end += 1

    else: # sum_n > target
        sum_n -= num_list[start]
        start += 1

print(check)