from collections import Counter

def solution(numbers):
    return sum(Counter(list(range(10))) - Counter(numbers))