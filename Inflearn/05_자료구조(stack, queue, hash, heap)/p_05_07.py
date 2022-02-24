'''
7. 교육과정 설계
현수는 1년 과정의 수업계획을 짜야 합니다.
수업중에는 필수과목이 있습니다. 이 필수과목은 반드시 이수해야 하며, 그 순서도 정해져 있습니다.
만약 총 과목이 A, B, C, D, E, F, G가 있고, 여기서 필수과목이 CBA로 주어지면 필수과목은
C, B, A과목이며 이 순서대로 꼭 수업계획을 짜야 합니다.
여기서 순서란 B과목은 C과목을 이수한 후에 들어야 하고,
A과목은 C와 B를 이수한 후에 들어야 한다는 것입니다.

필수과목순서가 주어지면 현수가 짠 N개의 수업설계가 잘된 것이면 “YES",
잘못된 것이면 ”NO“를 출력하는 프로그램
'''
from collections import deque
order_str = input()
num = int(input())

for n in range(num):
    order = deque(list(order_str))
    classes = input()
    result = "NO"

    for c in classes:
        if order and c == order[0]:
            order.popleft()
        elif order and c in order: # 필수과목 뒷 과목 먼저 들은 경우
            break


    if len(order) == 0:
        result = "YES"

    print('#{} {}'.format((n+1), result))