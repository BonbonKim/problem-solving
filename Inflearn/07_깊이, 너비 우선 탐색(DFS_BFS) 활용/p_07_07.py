'''
7. 송아지 찾기 (BFS : 상태 트리 탐색)
현수의 위치와 송아지의 위치가 직선상의 좌표 점으로 주어지면,
현수는 현재 위치에서 송아지의 위치까지 다음과 같은 방법으로 이동한다.
현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다.
(직선의 좌표 점은 1부터 10,000까지)

최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램
'''

from collections import deque

MAX = 10000
dist = [0] * (MAX + 1)  # 좌표 공간
check = [0] * (MAX + 1) # 방문 유무 체크

start, end = map(int, input().split())
visit_queue = deque([start]) # 첫 방문 좌표
check[start] = 1             # 첫 방문 좌표 체크

while True:
    now = visit_queue.popleft()

    if now == end:
        print(dist[now])
        break

    for next in (now+1, now-1, now+5):
        if 1 < next < 10000:
            if check[next] == 0:
                dist[next] = dist[now] + 1
                visit_queue.append(next)
                check[next] = 1