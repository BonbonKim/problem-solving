def solution(n):
    answer = ''
    num = ['4', '1', '2']

    while n:
        m, r = divmod(n, 3)
        answer = num[r] + answer
        n = m - (r == 0)
        print(m, r, n)

    return answer