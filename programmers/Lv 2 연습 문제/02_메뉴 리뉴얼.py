from itertools import combinations

def solution(orders, course):
    course_dict, answer= {}, []

    for order in orders:
        order = sorted(order)
        for c in course:
            tmp = list(combinations(order, c))
            for i in tmp:
                i = ''.join(i)
                course_dict[i] = course_dict.get(i, 0) + 1
    course_list = [(k, v) for k,v in course_dict.items() if v > 1]
    course_list.sort(key=lambda x: len(x))

    for c in course:
        tmp = [l for l in course_list if len(l[0]) == c]
        tmp.sort(key=lambda x: x[1], reverse=True)
        answer += [t[0] for t in tmp if t[1] == tmp[0][1]]

    return sorted(answer)