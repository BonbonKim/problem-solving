import math

def solution(answers):
    ps = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    correct, answer = [], []
    for p in ps:
        tmp = p * math.ceil(math.ceil(len(answers)/len(p)))
        cnt = sum([1 for i,j in zip(tmp,answers) if i==j])
        correct.append(cnt)
    answer = [i+1 for i in range(len(correct)) if correct[i]==max(correct)]
    return answer