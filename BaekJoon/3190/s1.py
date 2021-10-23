import sys
from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]
N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline().strip())
info = deque(list(sys.stdin.readline().split()) for _ in range(L))

mat = [[0]*(N+1) for _ in range(N+1)]
for apple in A:
    mat[apple[0]][apple[1]] = 1

snake = deque()
snake.append((1,1))
cnt = 0
idx = 1

change = int(info[0][0])
dir = info[0][1]
while True:
    cnt += 1
    head_y, head_x = snake[-1]
    head_y += dy[idx]
    head_x += dx[idx]

    if head_y < 1 or head_y > N or head_x < 1 or head_x > N: # 벽에 박으면
        break
    elif (head_y,head_x) in snake: # 몸에 박으면
        break
    snake.append((head_y,head_x))
    if mat[head_y][head_x] == 1:
        mat[head_y][head_x] = 0
    else:
        snake.popleft()

    if cnt == change: # 방향 바꾸기
        if dir == 'D':
            idx = (idx+1)%4
        else:
            idx = idx -1
            if idx == -1:
                idx = 3
        info.popleft()
        if info:
            change = int(info[0][0])
            dir = info[0][1]
print(cnt)