from collections import deque
import copy
def solution(priorities, location):
    max_pri = copy.deepcopy(priorities)
    max_pri.sort(reverse=True)
    max_pri = deque(max_pri)

    tmp_list = list()
    for i, num in enumerate(priorities):
        tmp_list.append((num, i))
    priorities = deque(tmp_list)

    cnt = 1
    absolute_length = len(priorities) # 우선 순위 큐 길이
    answer_dict = [0] * absolute_length
    while len(priorities) > 0:
        front = priorities.popleft()
        if front[0] < max_pri[0]:
            priorities.append(front)
        else:
            max_pri.popleft()
            answer_dict[front[1]] = cnt
            cnt += 1

        if answer_dict[location] > 0:
            return answer_dict[location]

if __name__ == "__main__":
    priorities = [9, 5, 4, 4, 6]
    loc = 3
    re = solution(priorities, loc)
    print(re)