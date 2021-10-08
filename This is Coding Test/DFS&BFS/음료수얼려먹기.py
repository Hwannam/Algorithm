N, M = map(int, input().split())

ice_map = [list(map(int,input())) for _ in range(N)]
def dfs(y, x):
    if x<0 or x>=M or y<0 or y>=N:
        return
    if ice_map[y][x] == 0:
        ice_map[y][x] = 1
        dfs(y-1,x)
        dfs(y + 1, x)
        dfs(y, x-1)
        dfs(y, x+1)
        return True

result = 0
for i in range(N):
    for j in range(M):
        if ice_map[i][j] == 0:
            if dfs(i,j):
                result += 1
print(result)