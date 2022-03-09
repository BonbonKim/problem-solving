def solution(numbers, hand):
    answer = ''
    dist = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,2)]
    left, right = 10, 11  # '*, #'

    for n in numbers:
        if dist[n][1] == 2:
            pick = 'R'
        elif dist[n][1] == 0:
            pick = 'L'
        else:
            s_r = dist[right]
            s_l = dist[left]
            e = dist[n]
            dist_r = abs(s_r[0]-e[0]) + abs(s_r[1]-e[1])
            dist_l = abs(s_l[0]-e[0]) + abs(s_l[1]-e[1])

            if dist_l == dist_r:
                pick = 'R' if hand == 'right' else 'L'
            else:
                pick = 'R' if dist_l > dist_r else 'L'
        answer += 'R' if pick == 'R' else 'L'
        right = n if pick == 'R' else right
        left = n if pick == 'L' else left

    return answer