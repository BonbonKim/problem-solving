from collections import Counter as c
def solution(n, lost, reserve):
    student = [1 for _ in range(n)]
    for i in lost:
        student[i-1] = 0
    for i in reserve:
        student[i-1] += 1

    for i in range(n):
        if student[i] != 2:
            continue
        if i-1 >= 0 and student[i-1] == 0:
            student[i], student[i-1] = 1, 1
            continue
        if i+1 < n and student[i+1] == 0:
            student[i], student[i+1] = 1, 1

    return n - c(student)[0]