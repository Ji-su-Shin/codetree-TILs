n = int(input())
students = dict()
attraction = [[-1] * n for _ in range(n)]

dir = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]

for _ in range(n*n):
    student = list(map(int, input().split(" ")))
    students[student[0]] = student[1:]

# 순서대로 앉히기
for current_student in students.keys():
    candidate_list = [] # 후보 위치 [x, y, 좋아하는 사람 수, 빈자리 수]
    max_like = -1
    max_empty = -1
    current_seat_x = -1
    current_seat_y = -1
    empty_min_row = n+1
    empty_min_col = n+1

    # 후보 자리 찾기
    for x in range(n):
        for y in range(n):
            # 가장 작은 row, col 빈자리 저장해두기 
            if attraction[x][y] == -1 and x < empty_min_row and y < empty_min_col :
                empty_min_row = x
                empty_min_col = y
            # 좋아하는 애, 빈 자리 탐색
            if(attraction[x][y] == -1):
                like = 0
                empty = 0
                for tmpX, tmpY in dir:
                    dx = x + tmpX
                    dy = y + tmpY
                    if dx >= 0 and dx < n and dy >= 0 and dy < n :
                        if attraction[dx][dy] == -1 : empty += 1
                        if attraction[dx][dy] in students[current_student] : like += 1
                # 후보로 올릴 것인가? 
                if like > max_like :
                    max_like = like
                    candidate_list.clear()
                    candidate_list.append([x, y, like, empty])
                elif like == max_like :
                    candidate_list.append([x, y, like, empty])
                
                
    # 후보가 여러 자리라면? - 인접한 칸 수 탐색
    if len(candidate_list) > 0 :
        for i in range(len(candidate_list)):
            if candidate_list[i][3] > max_empty:
                max_empty = candidate_list[i][3]
                current_seat_x = candidate_list[i][0]
                current_seat_y = candidate_list[i][1]
    # 하나도 후보가 없다면 - 행, 열 가장 작은 곳으로 선택
    elif len(candidate_list) == 0 :
        current_seat_x = empty_min_row
        current_seat_y = empty_min_col

    # 착석
    attraction[current_seat_x][current_seat_y] = current_student

# print(attraction)
# 점수 계산
score = 0
for x in range(n):
    for y in range(n):
        like = 0
        for dx, dy in dir:
            sx = x + dx
            sy = y + dy

            if sx >= 0 and sx < n and sy >= 0 and sy < n:
                if attraction[sx][sy] in students[attraction[x][y]]:
                    like += 1
        
        if like > 3:
            score += 1000
        elif like > 2:
            score += 100
        elif like > 1 :
            score += 10
        elif like > 0 :
            score += 1
        else :
            pass

print(score)