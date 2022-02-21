'''
4. 합이 같은 부분집합(DFS : 아마존 인터뷰)
N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때
두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력하고,
그렇지 않으면 ”NO"를 출력하는 프로그램
'''

def tree_traveral(i, right_list):
    if i == len_all_list:
        left_list = list(set(all_list) - set(right_list))

        if sum(left_list) == sum(right_list): # 두 부분 집합의 합 비교 -> 합이 같으면 YES
            global result
            result = "YES"
    else:
        num = all_list[i]

        # left list
        tree_traveral(i + 1, list(dict.fromkeys((right_list))))
        # right list
        right_list.append(num)
        tree_traveral(i + 1, list(dict.fromkeys((right_list))))


if __name__ == "__main__":
    result = "NO"
    len_all_list = int(input())
    all_list = list(map(int, input().split()))

    tree_traveral(0, list())
    print(result)
