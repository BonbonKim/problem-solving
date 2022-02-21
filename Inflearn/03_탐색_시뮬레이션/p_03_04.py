'''
4. 두 리스트 합치기
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램
'''

n = input()
list_n = list(map(int, input().split()))
m = input()
list_m = list(map(int, input().split()))

list_all = list_n + list_m
list_all = sorted(list_all)
print(" ".join(map(str, list_all)))