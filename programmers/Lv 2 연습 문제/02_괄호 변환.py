def isCorrect(u): #올바른 문자열?
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack: # 비어있을때, ')'부터 나오면
                return False
            else:
                stack.pop()
    return False if stack else True

def divid_p(w): # u,v로 분리
    balance = 0
    u, v = '', w
    for i in range(len(w)):
        balance += 1 if w[i] == '(' else -1
        if balance == 0:
            u = w[:i+1]
            v = w[i+1:] if i+1<len(w) else ''
            break
    return u, v

def solution(p): # 변환 과정(->올바른 문자열)
    if p == '':
        return ''

    u, v = divid_p(p)
    if isCorrect(u):
        return u + solution(v)
    else:
        tmp = ''
        for i in u[1:-1]:
            tmp += ')' if i=='(' else '('
        return '(' + solution(v) + ')' + tmp