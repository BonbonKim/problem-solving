'''
2. 쇠막대기
쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때,
잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램
'''

stick = input().replace('()','L') # 레이저
s, answer = 0, 0

for i in stick:
    if i == 'L':
        answer += s
    elif i == '(':
        s += 1
    else:
        s -= 1
        answer += 1

print(answer)
