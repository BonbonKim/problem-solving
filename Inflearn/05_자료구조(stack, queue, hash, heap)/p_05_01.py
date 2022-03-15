'''
1. 가장 큰 수 (스택)
숫자 하나가 주어졌을 때, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만드는 프로그램
-> 다시 풀기
'''

num, cnt = input().split()
cnt = int(cnt)
answer = []

for n in num:
    while answer and answer[-1]<n and cnt>0:
        answer.pop()
        cnt -= 1
    answer.append(n)

answer = answer[:-cnt] if cnt>0 else answer
print("".join(map(str, answer)))


