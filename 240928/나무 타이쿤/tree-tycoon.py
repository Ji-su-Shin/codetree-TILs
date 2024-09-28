import copy

# 변수 선언, 할당
n, m = map(int, input().split(" ")) # 칸 수, 년도
forest = []
rule = []
potion = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
potione_pre = []
total_height = 0

dir = [
    [0, 0],
    [0, 1], # 1
    [-1, 1], # 2
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1] # 8
]

cross_dir = [
    [1, 1],
    [-1, -1],
    [1, -1],
    [-1, 1]
]

for i in range(n):
    tree_height = list(map(int, input().split(" ")))
    forest.append(tree_height)

for i in range(m):
    rule_tmp = list(map(int, input().split(" ")))
    rule.append(rule_tmp)
    

# 로직
for current_year in range(m):
    # 영양제 이동
    x = dir[rule[current_year][0]][0] # x 이동 방향
    y = dir[rule[current_year][0]][1] # y 이동 방향
    cnt = rule[current_year][1] # 이동 횟수
    for i in range(len(potion)):
        px = potion[i][0] + (x * cnt) 
        py = potion[i][1] + (y * cnt)
        if px >= 0 : potion[i][0] = px % n
        else : potion[i][0] = px + n
        if py >= 0 : potion[i][1] = py % n
        else : potion[i][1] = py + n
        
    # 영양제 나무 성장
    for px, py in potion:
        forest[px][py] += 1

    # 대각선 버프
    for px, py in potion:
        for cx, cy in cross_dir:
            search_x = px + cx
            search_y = py + cy
            if search_x >= 0 and search_x < n and search_y >= 0 and search_y < n and forest[search_x][search_y] > 0:
                forest[px][py] += 1

    # 다 쓴 영양제 제거
    potion_pre = copy.deepcopy(potion)
    potion.clear()

    # 영양제 구매
    for x in range(n):
        for y in range(n):
            if ([x, y] not in potion_pre) and forest[x][y] >= 2:
                forest[x][y] -= 2
                potion.append([x, y])

    potion_pre.clear()


# 최종 나무 높이 출력
for x in range(n):
    total_height += sum(forest[x])

print(total_height)