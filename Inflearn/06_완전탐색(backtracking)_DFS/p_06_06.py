'''
6. 중복순열 구하기
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아
일렬로 나열하는 방법을 모두 출력하는 프로그램
'''

from itertools import product

num, pick_num = map(int, input().split())
num_list = list(range(1,num+1))

result = list(product(num_list, repeat=pick_num))

for r in result:
    print(" ".join(map(str, list(r))))
print(len(result))