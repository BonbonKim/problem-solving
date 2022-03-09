def solution(s):
    ex = [('zero', '0'), ('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'),
          ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')]
    for e in ex:
        s = s.replace(e[0], e[1])
    return int(s)