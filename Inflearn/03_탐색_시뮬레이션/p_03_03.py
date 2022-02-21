'''
3. 카드 역배치(정올 기출)
오름차순으로 한 줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면,
주어진 구간의 순서대로 위의 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤
마지막 카드들의 배치를 구하는 프로그램
'''

cards = list(range(1,21))

for i in range(10):
    section = list(map(int,input().split()))

    tmp = cards[section[0]-1: section[1]]
    tmp = list(reversed(tmp))

    cards[section[0]-1: section[1]] = tmp

print(" ".join(map(str, cards)))