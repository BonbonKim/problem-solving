from collections import Counter

def solution(numbers):
    answer = sum(Counter(list(range(10))) - Counter(numbers))
    return answer