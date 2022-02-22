'''
6. 응급실
- 환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자목록을 꺼냅니다.
- 나머지 대기 목록에서, 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로 다시 넣습니다.
  그렇지 않으면 진료를 받습니다.

현재 N명의 환자가 대기목록에 있습니다. N명의 대기목록 순서의 환자 위험도가 주어지면,
대기목록상의 M번째 환자는 몇 번째로 진료를 받는지 출력하는 프로그램
'''
import copy
from collections import deque

num, m = map(int, input().split())
num_list = list(map(int, input().split()))

risk_stack = copy.deepcopy(num_list)
risk_stack = sorted(risk_stack) # min_risk (r[0]) ~ max_risk (r[n])

pairs = [(i, value) for i, value in enumerate(num_list)]
queue = deque(pairs)

treat_cnt = 0
before_treat = True
while before_treat:
    turn = queue.popleft()

    if turn[1] == risk_stack[-1]:
        treat_cnt += 1
        risk_stack.pop()
        if turn[0] == m:
            break
    else:
        queue.append(turn)

print(treat_cnt)
