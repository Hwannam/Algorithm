import sys

dd = [(),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

def eat(y,x,info, result):
    global answer
    result += info[y][x][0]
    info[y][x][0] = -1 # 상어
    idx = info[y][x][1]
    cnt = 1
    while cnt <= 16:
        flag = False
        for i in range(4):
            for j in range(4):
                if info[i][j][0] == cnt:
                    moving = info[i][j][1]
                    dy, dx = dd[moving]
                    if 0<=i+dy<4 and 0<= j+dx < 4 and info[i+dy][j+dx][0] != -1:
                        info[i][j][0], info[i+dy][j+dx][0] = info[i+dy][j+dx][0], info[i][j][0]
                        info[i][j][1], info[i + dy][j + dx][1] = info[i + dy][j + dx][1], info[i][j][1]

                    else:
                        temp_cnt = 0
                        while temp_cnt < 8:
                            moving = moving + 1
                            temp_cnt += 1
                            if moving == 9:
                                moving = 1
                            dy, dx = dd[moving]
                            if 0 <= i + dy < 4 and 0 <= j + dx < 4 and info[i + dy][j + dx][0] != -1:
                                info[i][j][1] = moving
                                info[i][j][0], info[i + dy][j + dx][0] = info[i + dy][j + dx][0], info[i][j][0]
                                info[i][j][1], info[i + dy][j + dx][1] = info[i + dy][j + dx][1], info[i][j][1]
                                break
                    flag = True
                    break
            if flag:
                break
        cnt += 1
    ori_y = y
    ori_x = x
    while True:
        dy, dx = dd[idx]
        y += dy
        x += dx
        if y < 0 or y >= 4 or x <0 or x >= 4:
            break
        elif info[y][x][0] != 0:
            temp_info = []
            for item in info:
                tttt = []
                for k in item:
                    tttt.append(list(k))
                temp_info.append(tttt)
            temp_info[ori_y][ori_x][0] = 0
            eat(y,x, temp_info, result)
    answer = max(result, answer)

mat = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
answer = 0

arr = []
for i in range(4):
    temp = []
    for j in range(0,8,2):
        temp.append([mat[i][j],mat[i][j+1]])
    arr.append(temp)
eat(0,0,arr,0)
print(answer)
