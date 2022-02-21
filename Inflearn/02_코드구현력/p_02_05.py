'''
5. 정다면체
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
가장 확률이 높은 숫자를 출력하는 프로그램
'''

num_list = list(map(int, (input().split())))
N, M = num_list[0], num_list[1]
combi_dict = {}

for i in range(1, N+1):
    for j in range(1, M+1):
        sum_num = i+j
        if sum_num in combi_dict:
            combi_dict[sum_num] = combi_dict[sum_num] + 1
        else:
            combi_dict[sum_num] = 1

combi_dict = sorted(combi_dict.items(), key = lambda item:item[1], reverse=True)

results = list()
for i in range(len(combi_dict)):
    if combi_dict[0][1] != combi_dict[i][1]:
        break
    results.append(combi_dict[i][0])

print(" ".join(map(str, results)))