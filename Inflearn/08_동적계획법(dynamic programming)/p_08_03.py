'''
3. 도전과제 : 돌다리 건너기(Bottom-Up)
철수는 학교에 가는데 개울을 만났습니다. 개울은 N개의 돌로 다리를 만들어 놓았습니다.
철수는 돌 다리를 건널 때 한 번에 한 칸 또는 두 칸씩 건너뛰면서 돌다리를 건널 수 있습니다.
철수가 개울을 건너는 방법은 몇 가지일까요?
'''

def DFS(i):
    if climb_cnt[i] > 0:
        return climb_cnt[i]
    if i == 1 or i == 2:
        return i
    else:
        climb_cnt[i] = DFS(i-1) + DFS(i-2)
        return climb_cnt[i]

if __name__ == '__main__':
    num = int(input())
    climb_cnt = [0] * (47)

    DFS(num+2)
    print(climb_cnt[num+1]) # 돌다리 + 1 (건너편 땅)