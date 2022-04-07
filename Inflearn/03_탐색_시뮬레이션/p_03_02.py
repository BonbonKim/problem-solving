'''
2. 숫자만 추출
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만듭니다.
만들어진 자연수와 그 자연수의 약수 개수를 출력하는 프로그램
'''
# import re
#
# text = input()
# text = re.sub('[^0-9]', '', text)
#
# number = int(text)
#
# aliquot_list = [1, number] # 1, number
# for i in range(2, number):
#     if number % i == 0:
#         aliquot_list.append(i)
#
# list(dict.fromkeys(aliquot_list))
#
# print(number)
# print(len(aliquot_list))
import math
text = [i for i in input() if i.isdigit()]
num = int("".join(text))

cnt = [i for i in range(1,int(math.sqrt(num))+1) if num%i==0] # num의 제곱근까지 약수 개수(이 수와 짝꿍인 수도 있음 -> *2)
sqrt = -1 if int(math.sqrt(num))**2 == num else 0 # 25 = 5*5 -> 5 중복되니까 하나 제거
print(num, len(cnt)*2+sqrt, sep='\n')
