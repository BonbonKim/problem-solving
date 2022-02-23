'''
7. 가장 높은 탑 쌓기
밑면이 정사각형인 직육면체 벽돌들을 사용하여 탑을 쌓고자 한다. 탑은 벽돌을 한 개씩 아래에서 위로 쌓으면서 만들어 간다.
아래의 조건을 만족하면서 가장 높은 탑을 쌓을 수 있는 프로그램

(조건1) 벽돌은 회전시킬 수 없다. 즉, 옆면을 밑면으로 사용할 수 없다.
(조건2) 밑면의 넓이가 같은 벽돌은 없으며, 또한 무게가 같은 벽돌도 없다.
(조건3) 벽돌들의 높이는 같을 수도 있다.
(조건4) 탑을 쌓을 때 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다.
(조건5) 무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없다.
'''

num_len = int(input())
brick_list = list()
for data in range(num_len):
    brick_list.append(tuple(map(int, input().split())))

sort_1 = 0 # 넓이
sort_2 = 2 # 무게

brick_list.sort(key = lambda x: x[sort_1]) # 넓이 순으로 정렬(작은 수 ~ 큰 수)
dy = [0] * num_len # 누적 높이 기록
dy[0] = brick_list[0][1]

for i in range(1,num_len): # 무게 순으로 정렬
    cur_brick = brick_list[i]
    max_height = 0

    for j in range(0, i):
        if brick_list[j][sort_2] < cur_brick[sort_2] and max_height < dy[j]: # 무게 비교
            max_height = dy[j]

    dy[i] = max_height + cur_brick[1]

result_height = 0
for i in dy:
    if result_height < i:
        result_height = i

print(result_height)