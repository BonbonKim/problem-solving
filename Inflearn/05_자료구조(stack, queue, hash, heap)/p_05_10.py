'''
10. 최소힙
1) 자연수가 입력되면 최소힙에 입력한다.
2) 숫자 0 이 입력되면 최소힙에서 최솟값을 꺼내어 출력한다. (출력할 자료가 없으면 -1를 출력한다.)
3) -1이 입력되면 프로그램 종료한다.

최소힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램
'''

import heapq

result = list()
min_heap = list()

while True:
    num = int(input())

    if num > 0:
        heapq.heappush(min_heap, num)
    elif num == 0:
        result.append(heapq.heappop(min_heap))
    elif num == -1:
        print("\n".join(map(str, result)))
        break