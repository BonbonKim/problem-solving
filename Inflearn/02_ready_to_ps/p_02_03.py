'''
3. K번째 큰 수
1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있고, 3장을 뽑을 수 있는 모든 경우를 기록합니다.
기록한 값 중 K번째로 큰 수를 출력하는 프로그램
'''

num_list = list(map(int, input().split()))
N, K = num_list[0], num_list[1]
cards = list(map(int, input().split()))

cards.sort(reverse=True)
tmp = [0, 0, 0]
results = list()

for i in range(N):
    tmp[0] = cards[i]
    for j in range(N):
        if j > i:
            tmp[1] = cards[j]
            for z in range(N):
                if z > j:
                    tmp[2] = cards[z]
                    results.append(tmp[0]+tmp[1]+tmp[2])

results.sort(reverse=True)
results = list(dict.fromkeys(results))

print(results[K-1])