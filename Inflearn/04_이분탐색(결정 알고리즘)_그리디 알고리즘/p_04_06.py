'''
6. 씨름 선수 (그리디)
현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습니다.
현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다. 현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
“다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자만 뽑기로 했습니다.”
만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락입니다.

씨름 선수로 뽑히는 최대 인원을 출력하는 프로그램
'''
from collections import Counter
num_len = int(input())
people = list()

for i in range(num_len):
    people.append(tuple(map(int, input().split())))
# print(people)
people.sort(key=lambda x:x[0]) # 키 순서대로 정렬
# people.sort(key=lambda x: x[1], reverse=True)
# print(people)

out_list = [0] * num_len

for i in range(num_len):
     weight = people[i][1]
     if i < num_len-1 and out_list[i] == 0:
        for j in range(i+1,num_len):
            w = people[j][1]
            if weight < w:
                out_list[i] = 1

cnt = Counter(out_list)
print(cnt[0])

