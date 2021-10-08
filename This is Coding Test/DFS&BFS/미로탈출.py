N, M = map(int, input.split())

maze = [list(map(int, input())) for _ in range(N)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
def bfs(y,x):
    global result
    queue = []
    queue.append((y, x))

    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            else:



result = 0
bfs(0, 0)
print(result)