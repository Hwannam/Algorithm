import sys
from itertools import combinations
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def find_max(y, x, length, current_sum):
    global result
    current_sum += info[y][x]
    if length == 3:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0:
                temp = current_sum + info[ny][nx]
                if result < temp:
                    result = temp
        return
    visited[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<= nx < M and 0<=ny<N and visited[ny][nx] == 0:
            find_max(ny,nx,length+1,current_sum)
    visited[y][x] = 0

def mid_block(y, x):
    global result
    example = [0,1,2,3]
    for combi in combinations(example, 3):
        temp = info[y][x]
        for i in combi:
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < M and 0 <= ny < N:
                temp += info[ny][nx]
                result = max(result, temp)

N, M = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        find_max(i,j,1, 0)
        mid_block(i,j)
print(result)