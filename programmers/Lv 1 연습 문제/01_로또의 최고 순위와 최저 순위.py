from collections import Counter

def solution(lottos, win_nums):
    rank = list(range(7, 0, -1))
    rank[0] = 6

    correct_nums = len(list(set(lottos) & set(win_nums)))
    zero_nums = Counter(lottos)[0]

    return rank[correct_nums+zero_nums], rank[correct_nums]

