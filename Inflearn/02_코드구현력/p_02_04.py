'''
4. 대표값
N명의 학생의 수학 점수가 주어지면, N명의 학생들의 평균(소수 첫째 자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램

평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생 번호가 빠른 학생의 번호를 답으로 합니다.
'''

n = int(input())
nums = list(map(int, input().split()))
avg = int(round(sum(nums) / n, 0))

min_d, max_d = 100, -100
answer = -1

for i in range(len(nums)):
    d = nums[i] - avg
    if abs(d) < min_d or (abs(d) == min_d and max_d < d):
        answer = i+1
        min_d = abs(d)
        max_d = d

print(avg, answer)