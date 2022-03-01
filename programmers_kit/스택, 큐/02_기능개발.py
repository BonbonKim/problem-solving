def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()

    while progresses:
        cnt = 0
        while progresses and progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()
            cnt += 1

        if cnt > 0:
           answer.append(cnt)

        progresses = [progresses[i] + speeds[i] for i in range(len(speeds))]

    return answer