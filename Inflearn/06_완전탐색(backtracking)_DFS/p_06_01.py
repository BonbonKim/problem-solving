'''
1. 재귀함수를 이용한 이진수 출력
10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램 (재귀함수를 이용해서 출력)
'''

def divide_two(x, number_2):
    if x == 1:
        number_2.append(1)
    else:
        quotient = int(x / 2)
        reminder = x % 2

        divide_two(quotient, number_2)
        number_2.append(reminder)

if __name__ == "__main__":
    number_10 = int(input()) # 십진수
    number_2 = list()        # 이진수

    divide_two(number_10, number_2)

    print("".join(map(str,number_2)))

