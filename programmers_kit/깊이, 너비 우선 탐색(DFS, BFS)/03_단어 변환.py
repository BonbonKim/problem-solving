from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    inter_num = len(target) - 1  # 겹쳐야하는 알파벳 수
    Q = deque([(begin, 0)])  # next 단어 리스트

    while True:  # 한번에 하나씩만 바꿀 수 있게 안함
        cur_word = Q.popleft()

        if cur_word[0] == target:
            return cur_word[1]
        for word in words:
            intersection = list(set(list(cur_word[0])) & set(list(word)))  # 겹치는 알파벳 리스트(교집합)
            if len(intersection) == inter_num:
                Q.append((word, cur_word[1] + 1))

    return cur_word

if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    result = solution(begin, target, words)
    print(result) # 4