'''
10. 점수계산
시험문제의 채점 결과가 주어졌을 때, 총 점수를 계산하는 프로그램
'''

N = int(input())
score_list = list(map(int, input().split()))

result_sum = 0
accumu_cnt = 0
for i in range(N):
    cur_score = score_list[i]

    if cur_score == 1:
        accumu_cnt = accumu_cnt + 1
        result_sum += accumu_cnt
    else:
        accumu_cnt = 0

print(result_sum)