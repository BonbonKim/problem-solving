from math import gcd

def solution(arr):
    while len(arr) > 1:
        x = arr.pop()
        y = arr.pop()
        arr.append(x*y//gcd(x,y))
    return arr[0]