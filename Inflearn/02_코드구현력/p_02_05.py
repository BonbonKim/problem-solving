'''
5. 정다면체
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
가장 확률이 높은 숫자를 출력하는 프로그램
'''

from collections import Counter

n, m = map(int, input().split())
nums = []
for i in range(1, n+1):
    nums += [i+j for j in range(1, m+1)]

count = Counter(nums).most_common()
answer = [str(c[0]) for c in count if c[1]==count[0][1]]
print(" ".join(answer))