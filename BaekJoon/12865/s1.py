import sys

N, K = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
info.sort(key=lambda x:x[0])

mat = [[0]*(K+1) for _ in range(N)]
for i in range(N):
    for j in range(1, K+1):
        if i==0:
            if j >= info[0][0]:
                mat[0][j] = info[0][1]
        else:
            if j < info[i][0]:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = max(info[i][1]+mat[i-1][j-info[i][0]], mat[i-1][j])
print(mat[-1][-1])