import sys
dy = [0,1,0,-1]
dx = [-1,0,1,0]

left = [(-2,0,0.02),(-1,-1,0.1),(-1,0,0.07),(-1,1,0.01),(0,-2,0.05),(1,-1,0.1),(1,0,0.07),(1,1,0.01),(2,0,0.02)]
down = [(-y,x,z) for (y,x,z) in left]
right = [(y,-x,z) for (y,x,z) in left]
up = [(y,-x,z) for (y,x,z) in left]

N = int(input())
sand = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0
ny = N//2
nx = N//2
roop = 1
cnt = 0
idx = 0
while True:
    print(ny, nx)
    for _ in range(roop):
        print(ny,nx)
        ny = ny + dy[idx]
        nx = nx + dx[idx]
        if idx == 0:
            temp = left
        elif idx == 1:
            temp = down
        elif idx == 2:
            temp = right
        elif idx == 3:
            temp == up

        for move in temp:
            ky,kx,ratio = move
            if 0<=ny+ky<N and 0<=nx+kx<N:
                sand[ny+ky][nx+kx] += sand[ny][nx] * ratio
            else:
                result += sand[ny][nx] * ratio
    if ny == 0 and nx == 0:
        break

    cnt += 1
    idx = (idx+1)%4
    if cnt == 2:
        roop += 1
        cnt = 0

print(result)