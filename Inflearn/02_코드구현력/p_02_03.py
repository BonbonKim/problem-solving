'''
3. K번째 큰 수
1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있고, 3장을 뽑을 수 있는 모든 경우를 기록합니다.
기록한 값 중 K번째로 큰 수를 출력하는 프로그램
'''

from itertools import permutations

n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
nums = list(permutations(nums, 3))
nums = [sum(i) for i in nums]

print(sorted(set(nums),reverse=True)[k-1])
