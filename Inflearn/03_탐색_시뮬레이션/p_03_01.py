'''
1. 회문 문자열 검사
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)이면
YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램
'''

num_of_word = int(input())
results = ""

for i in range(num_of_word):
    is_equal = "YES"

    word = input().lower()
    word_list = list(word)

    len_word = len(word_list)
    split_num = int(len(word_list)/2)

    for j in range(split_num):
        if word_list[0+j] != word_list[len_word-1-j]:
            is_equal = "NO"
    results += "#{} {}\n".format((i+1),is_equal)

print(results)