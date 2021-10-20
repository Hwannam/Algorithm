import sys
sys.stdin = open('input.txt')

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def dfs(y,x):
    global result
    visited[y][x] = True
    if result == 1:
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not visited[ny][nx] and maze[ny][nx] != 1:
            visited[ny][nx] = True
            if maze[ny][nx] == 3:
                result = 1
            dfs(ny,nx)

for _ in range(1,11):
    result = 0
    tc = int(input())
    visited = [[False]*100 for _ in range(100)]
    maze = [list(map(int,input())) for _ in range(100)]
    dfs(1,1)
    print('#{} {}'.format(tc, result))