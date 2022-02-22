'''
1. 최대점수 구하기(DFS)
각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됩니다.
제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다.

제한 시간안에 얻을 수 있는 최대 점수를 출력하는 프로그램
'''

def calc_score(i, sum_score, sum_time):
    if sum_time > time_limit:
        return
    if i == num:
        global max_score
        if max_score < sum_score:
            max_score = sum_score
    else:
        calc_score(i + 1, sum_score, sum_time)
        calc_score(i + 1, sum_score + problem_list[i][0], sum_time + problem_list[i][1])

if __name__ == "__main__":
    problem_list = list()
    max_score = 0

    num, time_limit = map(int, input().split())
    for i in range(num):
        problem_list.append(tuple(map(int, input().split()))) # (score, time)

    calc_score(0, 0, 0)
    print(max_score)
