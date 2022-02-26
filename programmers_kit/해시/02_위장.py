def solution(clothes):
    clo_dict = dict()
    for clo in clothes:
        type = clo[1]
        clo_dict[type] = clo_dict.get(type, 0) + 1

    clo_nums = list(clo_dict.values())

    result = 1
    for c in clo_nums:
        result *= (c+1)
    result -= 1

    return result


if __name__ == '__main__':
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))
