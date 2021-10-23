import sys

N = int(sys.stdin.readline().strip())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N*N)]
aa = {}
for arr in S:
    aa[arr[0]] = arr[1:]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
room = [[0]*N for _ in range(N)]
room[1][1] = S[0][0]

idx = 1
while idx < N*N:
    cnt = -1
    blank = -1
    y = 0
    x = 0
    for i in range(N):
        for j in range(N):
            if room[i][j] == 0:
                temp_cnt = 0
                temp_blank = 0
                for k in range(4):
                    ni = i + dy[k]
                    nj = j + dx[k]
                    if 0<= ni < N and 0<= nj <N:
                        if room[ni][nj] in aa[S[idx][0]]:
                            temp_cnt += 1
                        elif room[ni][nj] == 0:
                            temp_blank += 1
                if temp_cnt > cnt:
                    y = i
                    x = j
                    cnt = temp_cnt
                    blank = temp_blank
                elif temp_cnt == cnt:
                    if temp_blank > blank:
                        y = i
                        x = j
                        cnt = temp_cnt
                        blank = temp_blank
    room[y][x] = S[idx][0]
    idx += 1

result = 0
for i in range(N):
    for j in range(N):
        count = 0
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if 0 <= ni < N and 0 <= nj < N:
                if room[ni][nj] in aa[room[i][j]]:
                    count += 1
        if count < 2:
            result += count
        else:
            result += 10**(count-1)
print(result)