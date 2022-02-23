'''
5. 최대 선 연결하기
왼쪽의 번호와 오른쪽의 번호가 있는 그림에서 같은 번호끼리 선으로 연결하려고 합니다.
왼쪽번호는 무조건 위에서부터 차례로 1부터 N까지 오름차순으로 나열되어 있습니다.
오른쪽의 번호 정보가 위부터 아래 순서로 주어지만 서로 선이 겹치지 않고 최대 몇 개의 선을 연결할 수 있는 지 구하는 프로그램
'''

num_len = int(input())
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

max_cnt = 0
for i in dy:
    if max_cnt < i:
        max_cnt = i
print(max_cnt)
