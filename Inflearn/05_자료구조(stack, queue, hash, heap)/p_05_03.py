'''
3. 후위표기식 만들기
중위표기식이 입력되면 후위표기식으로 변환하는 프로그램
'''

infix = input()
postfix = list()

stack = list()
oper = {'+':2, '-':2, '*':3, '/':3, '(':1, ')':1}

for i in infix:
    if i not in oper: # 숫자
        postfix.append(i)

    else:
        priority = oper[i]
        if stack and i != '(':
            if oper[stack[-1]] < priority:
                stack.append(i)
            else:
                while stack and oper[stack[-1]] >= priority:
                    postfix.append(stack.pop())
                stack.append(i)
        else:
            stack.append(i)

for i in range(len(stack)):
    postfix.append(stack.pop())

result = "".join(postfix)
result = result.replace('(', '').replace(')', '')
print(result)