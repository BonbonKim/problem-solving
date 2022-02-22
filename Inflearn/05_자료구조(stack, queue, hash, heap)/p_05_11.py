'''
11. 최대힙
1) 자연수가 입력되면 최대힙에 입력한다.
2) 숫자 0 이 입력되면 최대힙에서 최댓값을 꺼내어 출력한다. (출력할 자료가 없으면 -1를 출력한다.)
3) -1이 입력되면 프로그램 종료한다.

최대힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램
'''

import heapq

result = list()
max_heap = list()

while True:
    num = int(input())

    if num > 0:
        heapq.heappush(max_heap, (-num,num)) # (우선순위, 값) 양수값이 클수록, 음수값이 더 작아짐 (작은 수 == 우선순위 높음)
    elif num == 0:
        result.append(heapq.heappop(max_heap)[1])
    elif num == -1:
        print("\n".join(map(str, result)))
        break