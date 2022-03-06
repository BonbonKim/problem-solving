from collections import Counter

def solution(lottos, win_nums):
    answer = [0] * 2
    rank = list(range(7, 0, -1))
    rank[0] = 6

    correct_nums = len(list(set(lottos) & set(win_nums)))
    zero_nums = Counter(lottos)[0]

    answer[0] = rank[correct_nums+zero_nums]
    answer[1] = rank[correct_nums]

    return answer

