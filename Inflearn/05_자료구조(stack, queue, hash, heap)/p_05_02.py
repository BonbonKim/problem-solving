'''
2. 쇠막대기
쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때,
잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램
'''

pars = input()
pars = list(pars.replace("()", "L"))  # L : laser

stack = []
cnt = 0
for p in pars:
    if p == '(':
        stack.append('stick')
    elif p == ')':
        stack.pop()
        cnt += 1
    else: # L : laser
        cnt += len(stack)

print(cnt)