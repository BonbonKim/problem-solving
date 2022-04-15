cows = [[] for _ in range(11)]
n = int(input())
cnt = 0

for _ in range(n):
    cow, loc = map(int, input().split())
    cows[cow].append(loc)

for cow in cows:
    if len(cow) >= 2:
        tmp = ""
        for c in cow:
            if tmp != c:
                tmp = c
                cnt += 1
        cnt -= 1

print(cnt)