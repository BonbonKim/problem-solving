def solution(absolutes, signs):
    answer = 0
    for num, s in zip(absolutes,signs):
        answer += num if s else -num
    return answer