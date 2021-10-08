import sys
sys.stdin = open("input.txt")

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(y, x, temp):
    temp += background[y][x]
    if len(temp) == 7:
        num_list.add(temp)
        return
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            dfs(ny, nx, temp)

T = int(input())
for tc in range(T):
    background = [list(map(str, input().split())) for _ in range(4)]
    num_list = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, '')
    print("#{} {}".format(tc+1, len(num_list)))