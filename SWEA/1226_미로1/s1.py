import sys
sys.stdin = open("input.txt")

def bfs(sy, sx):
    queue = []
    queue.append((sy, sx))
    dyx = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 위, 오른쪽, 아래, 왼쪽 순서

    while queue:
        y, x = queue.pop(0)
        maze[y][x] = 1

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if 0 <= ny <= 15 and 0 <= nx <= 15:
                if maze[ny][nx] != 1:
                    queue.append((ny, nx))
                    if maze[ny][nx] == 3:
                        return 1
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sy = i
                sx = j
    print("#{} {}".format(tc, bfs(sy, sx)))