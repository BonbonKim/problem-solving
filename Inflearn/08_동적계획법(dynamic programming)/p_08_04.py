'''
4. 최대 부분 증가수열
N개의 자연수로 이루어진 수열이 주어졌을 때, 그 중에서 가장 길게 증가하는
(작은 수에서 큰 수로) 원소들의 집합을 찾는 프로그램
'''

num_len = input()
num_list = list(map(int, input().split()))

dy = [0] * num_len
dy[0] = 1

for i in range(1, num_len):
    cur_num = num_list[i]
    max_tmp = 0

    for j in range(0, i):
        if num_list[j] < cur_num and max_tmp < dy[j]:
            max_tmp = dy[j]

    dy[i] = max_tmp + 1

max_len = 0
for i in dy:
    if max_len < i:
        max_len = i
print(max_len)