'''
5. 회의실 배정 (그리디)
한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들
려고 한다. 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하
면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라. 단, 회의는 한번 시작하면 중간에 중
단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

첫째 줄에 최대 사용할 수 있는 회의 수를 출력하는 프로그램
'''


meeting_num = int(input())
meeting_list = list()
for i in range(meeting_num):
    meeting_list.append(tuple(map(int, input().split())))

meeting_list.sort(key = lambda x : (x[1], x[0]))

cnt = 0
prev_end = 0
for start, end in meeting_list:
    if start >= prev_end:
       cnt += 1
       prev_end = end

print(cnt)