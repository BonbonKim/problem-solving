'''
3. 뮤직비디오(결정알고리즘)
DVD에는 총 N개의 곡이 들어가는데, DVD에 녹화할 때에는 라이브에서의 순서가 그대로 유지되어야 한다.
또한 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.
M개의 DVD에 모든 동영상을 나눠서 녹화하기로 하였다.
이 때 DVD의 크기(녹화 가능한 길이)를 최소로 하려고 한다.
그리고 M개의 DVD는 모두 같은 크기여야한다.

DVD의 최소 용량 크기를 출력하는 프로그램
'''

def count_dvd(capacity):
    cnt = 1
    sum_music = 0
    for m in music_list:
        if sum_music + m > capacity:
            cnt += 1
            sum_music = m
        else:
            sum_music += m
    return cnt

music_num, dvd_num = map(int, input().split())
music_list = list(map(int, input().split()))
longest_music = max(music_list)

start = 1
end = sum(music_list)
result = end

while start <= end:
    mid = (start+end)//2

    if longest_music <= mid and count_dvd(mid) <= dvd_num: # 용량 더 줄일 수 있음
        result = min(mid, result)
        end = mid - 1
    else:
        start = mid + 1

print(result)