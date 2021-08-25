import sys
sys.stdin = open("input.txt")

def dfs(sy, sx):
    stack = [(sy, sx)]

    dyx = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 위, 오른쪽, 아래, 왼쪽 순서
    while stack:
        y, x = stack.pop()
        maze[y][x] = 1 # 이미 방문

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if maze[ny][nx] != 1:
                    if maze[ny][nx] == 3:
                        return 1
                    stack.append((ny, nx))
    return 0

T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N): # 시작 지점 찾기
        for j in range(N):
            if maze[i][j] == 2:
                sy = i
                sx = j
    result = dfs(sy, sx)
    print("#{} {}".format(tc+1, result))