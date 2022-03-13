def solution(record):
    states = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    ids = {}
    answer = []

    for r in record:
        r = r.split(" ")
        if r[0] in ['Enter', 'Change']:
            ids[r[1]] = r[2]

    for r in record:
        r = r.split(" ")
        if r[0] != 'Change':
            answer.append(ids.get(r[1]) + states.get(r[0]))

    return answer