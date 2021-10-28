import sys
dy = [0,1,0,-1]
dx = [-1,0,1,0]
indexing = {}
left = [(-2,0,0.02),(-1,-1,0.1),(-1,0,0.07),(-1,1,0.01),(0,-2,0.05),(1,-1,0.1),(1,0,0.07),(1,1,0.01),(2,0,0.02),(0,-1,0)]
down = [(-x,y,z) for (y,x,z) in left]
right = [(y,-x,z) for (y,x,z) in left]
up = [(x,y,z) for (y,x,z) in left]
direction = {0:left, 1:down, 2:right, 3:up}

def idx():
   x = (N+1) // 2-1
   y = (N+1) // 2-1
   index = 1
   turn = 0
   cnt = 0
   reach = 1
   temp = [[0]*N for _ in range(N)]
   while x>-1 and y >-1:
       indexing[index] = [y,x, turn]
       y += dy[turn]
       x += dx[turn]
       index += 1
       cnt += 1

       if cnt == reach:
           if turn == 1 or turn == 3:
               reach += 1
           turn = (turn+1)%4
           cnt = 0


def move(start):
    global result
    y, x, turnn = indexing[start+1]
    ss = sand[y][x]
    for moving in direction[indexing[start][2]]:
        dy, dx , ratio = moving
        ny = y +dy
        nx = x + dx
        if 0<= ny < N and 0<= nx < N:
            if ratio == 0:
                sand[ny][nx] += ss
            else:
                sand[ny][nx] += int(sand[y][x] * ratio)
                ss -= int(sand[y][x] * ratio)
        else:
            if ratio == 0:
                result += ss
            else:
                result += int(sand[y][x] * ratio)
                ss -= int(sand[y][x] * ratio)
    sand[y][x] = 0


N = int(input())
sand = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0
ny = N//2
nx = N//2
idx()

for i in range(1,N*N):
    move(i)
print(result)