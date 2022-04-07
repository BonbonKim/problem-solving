'''
1. 회문 문자열 검사
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)이면
YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램
'''

n = int(input())
for i in range(n):
    w = list(input().lower())
    rw = w[::-1]
    answer = "YES" if "".join(w) == "".join(rw) else "NO"
    print('#'+str(i+1),answer)
