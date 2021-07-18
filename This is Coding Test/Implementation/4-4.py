n, m = map(int,input().split())

x,y, direction = map(int,input().split())

visit = [[0]*m for _ in range(n)] 

visit[x][y] = 1

mapp = [[0]*m for _ in range(n)] 
for i in range(n):
   mapp[i] = list(map(int, input().split()))

def turn():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

dx = [0,1,0,-1]
dy = [-1,0,1,0]

count = 0
while True:
    turn()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if visit[nx][ny] ==0 and mapp[nx][ny]==0:
        x = nx
        y = ny
        visit[nx][ny] = 1
        count =0
    else:
        count+=1

    if count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if mapp[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        count = 0

result = 0
for i in range(len(visit)):
    for j in range(len(visit[i])):
        if visit[i][j] == 1:
            result+=1
print(result)
