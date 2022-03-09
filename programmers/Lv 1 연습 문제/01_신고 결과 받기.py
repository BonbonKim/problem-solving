from collections import Counter

def solution(id_list, report, k):
    report_dict = dict()  # key(신고당한 사람 str) : value(신고한 사람 list)

    for ids in report:
        user_id, rep_id = map(str, ids.split())

        if rep_id in report_dict:
            tmp = report_dict.get(rep_id)
            tmp.append(user_id)
            report_dict[rep_id] = tmp
        else:
            tmp = [user_id]
            report_dict[rep_id] = list(tmp)

    for i in report_dict:
        report_dict[i] = list(dict.fromkeys(report_dict[i]))
        if len(report_dict[i]) < k:
            report_dict[i] = []

    answer = [0] * len(id_list)
    mail = Counter(sum(list(report_dict.values()), []))

    for i in range(len(id_list)):
        answer[i] = mail[id_list[i]]
    return answer