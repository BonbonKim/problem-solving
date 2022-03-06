def solution(participant, completion):
    parti_dict = dict()

    for i in participant:
        parti_dict[i] = parti_dict.get(i, 0) + 1

    for i in completion:
        num = parti_dict.get(i)
        if num > 1:
            parti_dict[i] = num - 1
        else:
            del parti_dict[i]

    answer = list(parti_dict.keys())[0]

    return answer