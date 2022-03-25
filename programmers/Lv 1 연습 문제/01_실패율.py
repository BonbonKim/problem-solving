from collections import Counter

def solution(N, stages):
    answer = []
    cnt = Counter(stages)
    d = len(stages)

    for i in range(N):
        rate = cnt[i+1]/d  if cnt[i+1]>0 and d>0 else 0
        answer.append([i+1, rate])
        d -= cnt[i+1]

    answer.sort(key=lambda x:x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer