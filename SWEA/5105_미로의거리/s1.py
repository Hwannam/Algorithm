import sys
sys.stdin = open("input.txt")

def bfs(sy, sx):
    queue = []
    distance = [[0] * (N) for _ in range(N)]
    queue.append((sy, sx))
    dyx = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 위, 오른쪽, 아래, 왼쪽 순서

    while queue:
        y, x = queue.pop(0)
        maze[y][x] = 1

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if 0 <= ny <= N - 1 and 0 <= nx <= N - 1:
                if maze[ny][nx] != 1:
                    queue.append((ny, nx))
                    distance[ny][nx] = distance[y][x] + 1
                    if maze[ny][nx] == 3:
                        return distance[ny][nx] - 1 # 통과한 칸 수를 체크하니까 도착점 제외
    return 0

T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy = i
                sx = j
    print("#{} {}".format(tc + 1, bfs(sy, sx)))