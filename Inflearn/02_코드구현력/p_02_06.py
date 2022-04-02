'''
6. 자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고,
그 합이 최대인 자연수를 출력하는 프로그램
'''

nums_len = int(input())
nums = list(input().split())

for i in range(nums_len):
    sum_n = sum(list(map(int, nums[i])))
    nums[i] = [nums[i], sum_n]

nums.sort(reverse=True, key=lambda x: x[1])
print(nums[0][0])
