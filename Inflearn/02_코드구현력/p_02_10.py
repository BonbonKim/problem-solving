'''
10. 점수계산
시험문제의 채점 결과가 주어졌을 때, 총 점수를 계산하는 프로그램
'''

_ = input()
num = list(map(int,input().split()))

answer = [0]
for n in num:
    if n == 0:
        answer.append(0)
    else:
        answer.append(answer[-1]+1)
print(sum(answer))