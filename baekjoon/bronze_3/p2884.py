h, m = map(int, input().split())

h = h if m>=45 else h-1
h = 23 if h<0 else h
m = m-45 if m>=45 else 15+m
print(h, m)
