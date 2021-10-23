import sys
dy = [0,0,0,-1,1]
dx = [0,1,-1,0,0]

dice = [0,0,0,0,0,0,0]
N,M,y,x,K = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order = list(map(int, sys.stdin.readline().split()))

for number in order:
    if 0<= y+dy[number] < N and 0<= x+dx[number] < M:
        y += dy[number]
        x += dx[number]
        if number == 1:
            dice[1], dice[3] = dice[3], dice[1]
            dice[1], dice[4] = dice[4], dice[1]
            dice[4], dice[6] = dice[6], dice[4]
        elif number == 2:
            dice[4], dice[6] = dice[6], dice[4]
            dice[4], dice[3] = dice[3], dice[4]
            dice[1], dice[4] = dice[4], dice[1]
        elif number == 3:
            dice[1], dice[2] = dice[2], dice[1]
            dice[2], dice[5] = dice[5], dice[2]
            dice[2], dice[6] = dice[6], dice[2]
        elif number == 4:
            dice[1], dice[2] = dice[2], dice[1]
            dice[1], dice[6] = dice[6], dice[1]
            dice[1], dice[5] = dice[5], dice[1]

        if info[y][x] == 0:
            info[y][x] = dice[6]
        else:
            dice[6] = info[y][x]
            info[y][x] = 0
        print(dice[1])