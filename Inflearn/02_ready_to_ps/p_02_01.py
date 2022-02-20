'''
1. K번째 약수
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램
'''

N, K = input().split()
N, K = int(N), int(K)
num_list = list()

for i in range(1, N+1):
    if N % i == 0:
        num_list.append(i)
num_list.sort()

if len(num_list) < K-1:
    print(-1)
else:
    print(num_list[K-1])


