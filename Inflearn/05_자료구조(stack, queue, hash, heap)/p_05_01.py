'''
1. 가장 큰 수 (스택)
숫자 하나가 주어졌을 때, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만드는 프로그램
-> 다시 풀기
'''

digit, cut_num = map(str, input().split())
cut_num = int(cut_num)

digit = list(map(int, list(digit)))

new_digit = []
for d in digit:
    while new_digit and new_digit[-1] < d and cut_num > 0:
        new_digit.pop()
        cut_num -= 1
    new_digit.append(d)

if cut_num != 0: # 한번 돌 때, m개 만큼 다 지우지 못한 경우, 맨 뒤에서 자르기
    new_digit[:-cut_num]

new_digit = "".join(map(str, new_digit))
print(new_digit)


