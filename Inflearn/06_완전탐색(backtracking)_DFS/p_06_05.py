'''
5. 바둑이 승차
철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운
무게를 구하는 프로그램
'''

def calc_weight(i, sum_w, acc_w): # sum_of_weight, accumulate_of_weight
    global max_weight
    if (total_w - acc_w) + sum_w < max_weight:
        return
    if sum_w > weight_limit:
        return
    if i == num_of_dog:
        if max_weight < sum_w:
            max_weight = sum_w
    else:
        calc_weight(i + 1, sum_w, acc_w + dog_weights[i])
        calc_weight(i + 1, sum_w + dog_weights[i], acc_w + dog_weights[i])


if __name__ == "__main__":
    weight_limit, num_of_dog = map(int, input().split())
    dog_weights = [0] * num_of_dog

    for i in range(num_of_dog):
        dog_weights[i] = int(input())

    total_w = sum(dog_weights) # total_weight
    max_weight = 0

    calc_weight(0, 0, 0)
    print(max_weight)
