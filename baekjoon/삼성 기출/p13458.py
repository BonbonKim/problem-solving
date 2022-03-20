# 시험 감독 https://www.acmicpc.net/problem/13458

import math

n = int(input())
apps = list(map(int, input().split()))
b, c = map(int, input().split())

for i in range(len(apps)):
    n += math.ceil((apps[i] - b) / c) if apps[i]-b > 0 else 0
print(n)