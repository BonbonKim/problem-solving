'''
9. 주사위 게임
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.

N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램
'''

num_of_people = int(input())
award_list = list()

for n in range(num_of_people):
    dice_list = list(map(int, input().split()))
    count_dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    for i in dice_list:
        count_dice[i] = count_dice[i] + 1

    award = 0
    for i in count_dice.keys():
        if count_dice[i] == 3:
            award = 10000 + (1000 * i)
            break
        elif count_dice[i] == 2:
            award = 1000 + (100 * i)
            break
        elif count_dice[i] == 1:
            award = 100 * i
    award_list.append(award)


award_list.sort()
print(award_list[-1])
