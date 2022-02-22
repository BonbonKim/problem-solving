import copy

cnt = 0

def make_target(i, numbers, target):
    global cnt
    answer = sum(numbers)

    if i == len(numbers):
        if answer == target:
            cnt += 1
    else:
        new_numbers = copy.deepcopy(numbers)
        new_numbers[i] = -new_numbers[i]
        make_target(i + 1, numbers, target)
        make_target(i + 1, new_numbers, target)

def solution(numbers, target):
    global cnt
    make_target(0, numbers, target)
    return cnt

if __name__ == "__main__":
    numbers = [1,1,2,1]
    target = 3

    cnt = solution(numbers, target)
    print(cnt) # 3