dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

n = int(input())
students = [list(map(int, input().split())) for _ in range(n**2)]
like_students = [0] * (n**2 + 1) # 각 학생이 좋아하는 친구 리스트
classrooms = [[0] * n for _ in range(n)] # 실제 학생의 위치

for i in range(len(students)):
    students[i] = (students[i][0], students[i][1:5])

for s in students:
    num, like = s[0], s[1]
    like_students[num] = like
    check = []

    for r in range(n):
        for c in range(n):
            if classrooms[r][c] != 0:
                continue
            cnt_like, cnt_null = 0, 0

            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]
                if rr<0 or rr>n-1 or cc<0 or cc>n-1:
                    continue
                cnt_null = cnt_null + (classrooms[rr][cc] == 0)
                cnt_like = cnt_like + (classrooms[rr][cc] in like)
            check.append([(r,c), cnt_null, cnt_like])

    check.sort(key=lambda x: (x[2], x[1]), reverse=True)
    check = [c for c in check if check[0][1:3]==c[1:3]]
    check.sort(key=lambda x: (x[0][0], x[0][1]))

    r, c = check[0][0]
    classrooms[r][c] = num


answer = 0
for r in range(n):
    for c in range(n):
        num, cnt_like =  classrooms[r][c], 0

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if rr<0 or rr>n-1 or cc<0 or cc>n-1:
                continue
            cnt_like = cnt_like + (classrooms[rr][cc] in like_students[num])
        answer = answer + (10**(cnt_like-1)) * (cnt_like>=1)

print(int(answer))