'''
5. 공주 구하기(큐)
1번 왕자부터 N번 왕자까지 순서대로 시계 방향으로 돌아가며 동그랗게 앉게 한다.
그리고 1번 왕자부터 시계 방향으로 돌아가며 1부터 시작하여 번호를 외치게 한다.
한 왕자가 K(특정 숫자)를 외치면 그 왕자는 공주를 구하러 가는데서 제외되고 원 밖으로 나오게 된다.
그리고 다음 왕자부터 다시 1부터 시작하여 번호를 외친다.

N과 K가 주어질 때, 공주를 구하러 갈 왕자의 번호를 출력하는 프로그램
'''

from collections import deque

n, k = map(int, input().split())
q = deque(list(range(1, n+1)))

while len(q) > 1:
    for i in range(k-1):
        tmp = q.popleft()
        q.append(tmp)
    q.popleft()
print(q[0])