'''
1. 이분검색
임의의 N개의 숫자가 입력으로 주어집니다.
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면
이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램
'''

num_len, target = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

start = 0
end = num_len
while True:
    mid = (start+end)//2

    if num_list[mid] == target:
        print(mid+1)
        break
    else:
        if num_list[mid] < target:
            start = mid+1
        else:
            end = mid-1