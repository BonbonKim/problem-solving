'''
2. 랜선 자르기 (결정 알고리즘)
K개의 랜선은 길이가 제각각이다. 선생님은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에
K개의 랜선을 잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면
20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
이때, 만들 수 있는 최대 랜선의 길이를 구하는 프로그램
'''

num_len, target = map(int, input().split())
num_list = list()

largest = 0
for i in range(num_len):
    tmp = int(input())
    num_list.append(tmp)
    largest = max(tmp, largest)

start = 1
end = largest
max_len = 0 # 최대 랜선 길이 (가장 큰 값으로 찾기)

while start <= end:
    mid = (start+end)//2 # 이 길이로 랜선 자르기 (mid : 현재 길이)

    cnt = 0 # 만든 랜선 개수
    for num in num_list:
        cnt += num//mid

    if target <= cnt:
        max_len = max(mid, max_len)
        start = mid + 1
    else:
        end = mid-1

print(max_len)