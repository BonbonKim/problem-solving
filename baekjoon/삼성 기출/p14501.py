# 퇴사 https://www.acmicpc.net/problem/14501

def DFS(i, rest_time, total_fee):
    global max_fees
    if i == n:
        if max_fees < total_fee:
            max_fees = total_fee
    else:
        if rest_time <= 0 and i+times[i] <= n: # 1+1 <=2
            DFS(i + 1, times[i] - 1, total_fee + fees[i])
            DFS(i + 1, 0, total_fee)
        else:
            DFS(i+1, rest_time-1, total_fee)


n = int(input())
times = [0] * n
fees = [0] * n

for i in range(n):
    times[i], fees[i] = map(int, input().split())

max_fees = 0
DFS(0, 0, 0)
print(max_fees)
