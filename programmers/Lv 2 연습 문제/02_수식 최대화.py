import copy
from itertools import permutations

def solution(expression):
    expression = expression.replace('-',' - ').replace('+',' + ').replace('*',' * ').split(' ')
    opers = list(permutations(['+', '-', '*'], 3))
    answer = 0

    for oper in opers:
        eq = copy.deepcopy(expression)
        for o in oper:
            while o in eq:
                idx = eq.index(o)
                tmp = eval(''.join(eq[idx-1:idx+2]))
                eq[idx-1:idx+2] = 'T'
                eq[idx-1] = str(tmp)
        answer = abs(int(eq[0])) if abs(int(eq[0])) > answer else answer
    return answer