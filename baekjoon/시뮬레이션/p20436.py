keyboard = {'q':[0,0], 'w':[0,1], 'e':[0,2], 'r':[0,3], 't':[0,4], 'y':[0,5], 'u':[0,6], 'i':[0,7], 'o':[0,8], 'p':[0,9],
            'a':[1,0], 's':[1,1], 'd':[1,2], 'f':[1,3], 'g':[1,4], 'h':[1,5], 'j':[1,6], 'k':[1,7], 'l':[1,8],
            'z':[2,0], 'x':[2,1], 'c':[2,2], 'v':[2,3], 'b':[2,4], 'n':[2,5], 'm':[2,6]}
korean_vowel = ['y','u','i','o','p','h','j','k','l','b','n','m'] # right

left, right = map(str, input().split())
text = input()

time = 0
for now in text:
    nx, ny = keyboard.get(now)
    time += 1

    if now in korean_vowel:
        rx, ry = keyboard.get(right)
        time_r = abs(rx - nx) + abs(ry - ny)
        time += time_r
        right = now
    else:
        lx, ly = keyboard.get(left)
        time_l = abs(lx-nx) + abs(ly-ny)
        time += time_l
        left = now

print(time)