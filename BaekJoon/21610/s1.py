import sys

direction = [(),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
daegak = [(1,1),(-1,-1),(-1,1),(1,-1)]
def move(idx):
    global clouds
    if idx == M:
        return
    d, s = info[idx]
    dy, dx = direction[d]
    check = [[0]*N for _ in range(N)]
    for cloud in clouds:
        cloud[0] += dy*s
        cloud[1] += dx*s
        if cloud[0] < 0:
            temp = (-cloud[0])%N
            cloud[0] = N-temp
            if cloud[0] == N:
                cloud[0] = 0
        elif cloud[0] >= N:
            cloud[0] %= N
        if cloud[1] < 0:
            temp = (-cloud[1]) % N
            cloud[1] = N - temp
            if cloud[1] == N:
                cloud[1] = 0
        elif cloud[1] >= N:
            cloud[1] %= N
        numbers[cloud[0]][cloud[1]] += 1 # 물 증가
        check[cloud[0]][cloud[1]] = 1

    for cloud in clouds:
        daegak_cnt = 0
        for i in range(4):
            a = cloud[0] + daegak[i][0]
            b = cloud[1] + daegak[i][1]
            if 0<= a < N and 0<= b < N:
                if numbers[a][b] > 0:
                    daegak_cnt += 1
        numbers[cloud[0]][cloud[1]] += daegak_cnt

    temp_cloud = []
    for i in range(N):
        for j in range(N):
            if numbers[i][j] >= 2 and check[i][j] == 0:
                numbers[i][j] -= 2
                temp_cloud.append([i,j])
    clouds = [i[:] for i in temp_cloud]
    move(idx+1)

N, M = map(int, sys.stdin.readline().split())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
info = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

clouds = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
move(0)

result = 0
for row in numbers:
    result += sum(row)
print(result)