'''
8. 단어 찾기 (hash)
현수는 영어로 시는 쓰는 것을 좋아합니다.
현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다.
이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다.

두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고,
이어 바로 다음 줄부터 시에 쓰인 N-1개의 단어가 주어진다.
첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력하는 프로그램
'''

num = int(input())

words = dict()
for i in range(num):
    w = input()
    words[w] = 1

for i in range(num-1):
    w = input()
    words[w] = 0 # 시에 사용됐으면 -1

for k, v in words.items():
    if v == 1:
        print(k)

