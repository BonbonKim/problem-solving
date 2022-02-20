'''
2. K번째 수
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램
'''
T = int(input())
result = ""

for t in range(T):
    num_list = list(map(int, input().split()))
    N, s, e, k = num_list[0], num_list[1], num_list[2], num_list[3]
    nums = list(map(int, input().split()))
    tmp = nums[s-1:e]
    tmp.sort()
    result += str(t+1)+" "+str(tmp[k-1])+"\n"

print(result.strip())
