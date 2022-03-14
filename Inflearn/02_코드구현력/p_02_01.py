'''
1. K번째 약수
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램
'''

n, k = map(int, input().split())
num = [i for i in range(1, n+1) if n%i == 0]

answer = num[k-1] if len(num)>=k else -1
print(answer)