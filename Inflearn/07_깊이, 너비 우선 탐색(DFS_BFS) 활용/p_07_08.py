'''
8. 사과나무 (BFS)
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다.
N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사과를 수확할 때,
다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다

현수과 수확하는 사과의 총 개수를 출력하는 프로그램
'''

num = int(input())
board_digit = list()
board_check = list()
for i in range(num):
    board_digit.append(list(map(int, input().split())))

sum = 0
center = num//2
check = list()

for x in range(num):
    if x == 0:
        check.append(center)
    elif x <= center:
        check.append(center-x)
        check.append(center+x)
        check.sort()
    else:
        check.remove(check[0])
        check.remove(check[-1])

    for y in check:
       sum += board_digit[x][y]

print(sum)


