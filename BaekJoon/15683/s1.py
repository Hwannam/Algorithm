import sys
from itertools import combinations
directions = [(0,1),(0,-1),(1,0),(-1,0)]
cctv1 = list(combinations(directions,1))
cctv2 = [((0,-1),(0,1)), ((1,0),(-1,0))]
cctv3 = [((-1,0),(0,1)),((0,1),(1,0)),((1,0),(0,-1)),((0,-1),(-1,0))]
cctv4 = list(combinations(directions,3))
cctv5 = list(combinations(directions,4))
cctv_list = {1:cctv1, 2:cctv2, 3:cctv3, 4:cctv4, 5:cctv5}

def check_camera(camera_list, idx, blank):
    global result, info
    if idx >= len(camera_list):
        result = min(blank, result)
        return
    y,x,camera_num = camera_list[idx]
    current_camera = cctv_list[camera_num]
    for directs in current_camera:
        temp = [i[:] for i in info]
        temp_blank = blank
        for direct in directs:
            dy, dx = direct
            ny = y
            nx = x
            while True:
                ny += dy
                nx += dx
                if 0 <= ny < N and 0 <= nx < M:
                    if info[ny][nx] == 0:
                        info[ny][nx] = 7
                        blank -= 1
                    elif info[ny][nx] == 6:
                        break
                else:
                    break
        check_camera(camera_list, idx+1, blank)
        info = temp
        blank = temp_blank


N, M = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
camera_list = []
result = N*M
blank = 0
for i in range(N):
    for j in range(M):
        if info[i][j] != 6 and info[i][j] != 0:
            camera_list.append((i,j,info[i][j]))
        elif info[i][j] == 0:
            blank+=1
check_camera(camera_list, 0, blank)
print(result)