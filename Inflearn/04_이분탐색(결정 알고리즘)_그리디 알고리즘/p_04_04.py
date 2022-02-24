'''
4. 마구간 정하기 (결정 알고리즘)
N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며,
마구간 간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다.
각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을
마구간에 배치하고 싶습니다.

C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대
값을 출력하는 프로그램
'''

room, horse_num = map(int, input().split())
room_list = list()
for _ in range(room):
    room_list.append(int(input()))

room_list.sort()
start = room_list[0]
end = room_list[-1]
max_dist = 0

while start <= end:
    mid = (start+end)//2 # 가장 가까운 두 말의 최대 거리 -> 모든 말은 이거보다 서로 멀어야 됨
    horse_cnt = 1
    horse_pos = room_list[0]

    for i in room_list:
        if i-horse_pos >= mid:
            horse_cnt += 1
            horse_pos = i

    if horse_cnt < horse_num:
        end = mid - 1
    else:
        start = mid + 1
        max_dist = max(mid,max_dist)

print(max_dist)