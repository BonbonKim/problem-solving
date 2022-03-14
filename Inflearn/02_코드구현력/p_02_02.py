'''
2. K번째 수
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램
'''

t = int(input())

for i in range(t):
    _, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    print('#'+str(i+1),sorted(num[s-1:e])[k-1])
