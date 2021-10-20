import sys
from itertools import combinations
from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs(walls, cnt):
    global result
    temp_map = [i[:] for i in info]
    for wall in walls:
        y = wall[0]
        x = wall[1]
        temp_map[y][x] = 1
    queue = deque()
    for virus in viruses:
        y = virus[0]
        x = virus[1]
        queue.append((y,x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and temp_map[ny][nx] == 0:
                temp_map[ny][nx] = 2
                queue.append((ny,nx))
                cnt -= 1
    if cnt > result:
        result = cnt

N, M = map(int, sys.stdin.readline().split())
info = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
blank = []
viruses = []
blank_cnt = -3
for i in range(N):
    for j in range(M):
        if info[i][j] == 0:
            blank.append((i,j))
            blank_cnt += 1
        elif info[i][j] == 2:
            viruses.append((i,j))

result = 0
add_walls = list(combinations(blank, 3))
for add_wall in add_walls:
    bfs(add_wall, blank_cnt)
print(result)