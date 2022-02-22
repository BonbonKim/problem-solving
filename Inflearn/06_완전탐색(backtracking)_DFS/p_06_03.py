'''
3. 부분집합 구하기(DFS)
자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램
'''

def tree_traveral(i, data):
    if i > number:
        print(data)
    else:
        new_data_O = data + " " + str(i)
        new_data_X = data
        tree_traveral(i + 1, new_data_O)
        tree_traveral(i + 1, new_data_X)

if __name__ == "__main__":
    number = int(input())
    tree_traveral(1, "")
