import sys

direct = [(0,1),(-1,0),(0,-1),(1,0)]

N = int(sys.stdin.readline().strip())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plain = [[0]*101 for _ in range(101)]

for i in range(N):
    x,y,d,g = info[i]

    plain[y][x] = 1
    curve = [d]
    for _ in range(g):
        curve += [(k + 1) % 4 for k in curve[::-1]]

    for k in curve:
        y = y+direct[k][0]
        x = x+direct[k][1]
        plain[y][x] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if plain[i][j] + plain[i][j+1] + plain[i+1][j] + plain[i+1][j+1] == 4:
            cnt += 1
print(cnt)