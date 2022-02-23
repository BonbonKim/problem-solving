'''
2. 네트워크 선 자르기(Top-Down : 재귀, 메모이제이션)

4m의 네트워크 선이 주어진다면, 아래의 5가지 방법을 생각할 수 있습니다.
1) 1m+1m+1m+1m, 2) 2m+1m+1m, 3) 1m+2m+1m, 4) 1m+1m+2m, 5) 2m+2m
네트워크 선의 길이가 Nm라면, 몇 가지의 자르는 방법을 생각할 수 있나요?
'''

def DFS(i):
    if cut_cnt[i] > 0:
        return cut_cnt[i]
    if i == 1 or i == 2:
        return i
    else:
        cut_cnt[i] = DFS(i-1) + DFS(i-2)
        return cut_cnt[i]

if __name__ == '__main__':
    num = int(input())
    cut_cnt = [0] * (46)

    DFS(num)
    print(cut_cnt[num])