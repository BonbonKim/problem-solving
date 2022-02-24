'''
7. 창고 정리
창고 높이 조정은 가장 높은 곳에 상자를 가장 낮은 곳으로 이동하는 것을 말한다.
가장 높은 곳이나 가장 낮은 곳이 여러곳이면 그 중 아무거나 선택하면 된다.
창고의 가로 길이와 각 열의 상자 높이가 주어집니다.

m회의 높이 조정을 한 후 가장 높은 곳과 가장 낮은 곳의 차이를 출력하는 프로그램
'''

num = int(input())
num_list = list(map(int, input().split()))
turn = int(input())

num_list.sort()

for _ in range(turn):
    num_list[0] += 1
    num_list[-1] -= 1
    num_list.sort()

print(num_list[-1] - num_list[0])