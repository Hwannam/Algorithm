import sys

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(r,c,d):
    global result, end
    if end == True:
        return
    if place[r][c] == 0:
        place[r][c] = 2
        result += 1

    for _ in range(4):
        d -= 1
        if d == -1:
            d = 3
        ny = r + dy[d]
        nx = c + dx[d]
        if place[ny][nx] == 0:
            dfs(ny, nx, d)
    if place[r+dy[(d+2)%4]][c+dx[(d+2)%4]] == 1:
        end = True
        return
    else:
        dfs(r+dy[(d+2)%4],c+dx[(d+2)%4],d)


N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
place = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 0
end = False
dfs(r,c,d)
print(result)
