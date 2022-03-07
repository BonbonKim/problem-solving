import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for s in scoville:
        heapq.heappush(h, s)

    while h[0] < K:
        m1 = heapq.heappop(h)
        m2 = heapq.heappop(h)
        heapq.heappush(h, m1+(m2*2))
        answer += 1
        if len(h) == 1 and h[0] < K:
            return -1

    return answer