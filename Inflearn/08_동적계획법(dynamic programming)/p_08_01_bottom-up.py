'''
1. 동적계획법이란? 네트워크 선 자르기(Bottom-Up)
4m의 네트워크 선이 주어진다면, 아래의 5가지 방법을 생각할 수 있습니다.
1) 1m+1m+1m+1m, 2) 2m+1m+1m, 3) 1m+2m+1m, 4) 1m+1m+2m, 5) 2m+2m
네트워크 선의 길이가 Nm라면, 몇 가지의 자르는 방법을 생각할 수 있나요?
'''

cut_cnt = [0] * (46)
cut_cnt[1] = 1
cut_cnt[2] = 2

num = int(input())

for i in range(3, num+1):
    cut_cnt[i] = cut_cnt[i-2] + cut_cnt[i-1]

print(cut_cnt[num])