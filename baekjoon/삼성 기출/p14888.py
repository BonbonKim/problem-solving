from itertools import permutations

num_len = int(input())
num = list(map(str, input().split()))

oper_len = list(map(int, input().split()))
oper = ['+']*oper_len[0] + ['-']*oper_len[1] + ['*']*oper_len[2] + ['//']*oper_len[3]

oper_permut = list(set(permutations(oper, sum(oper_len))))
answer = []

for o in oper_permut:
    result = num[0]
    for i in range(1, len(num)):
        if o[i-1]=='//' and int(result)<0:
            result = -eval(str(abs(int(result)))+o[i-1]+num[i])
        else:
            result = eval(str(result)+o[i-1]+num[i])
    answer.append(result)

print(max(answer))
print(min(answer))