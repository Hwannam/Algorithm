import sys
from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs(y,x):
    moved = False
    queue = deque()
    visited = []
    queue.append((y, x))
    visited.append((y,x))
    temp = people[y][x]
    real_visited[y][x] = 1
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < N and 0<= nx < N and (ny,nx) not in visited and real_visited[ny][nx] == 0:
                if L <= abs(people[ny][nx] - people[y][x])<=R:
                    moved = True
                    visited.append((ny,nx))
                    queue.append((ny,nx))
                    temp += people[ny][nx]
                    real_visited[ny][nx] = 1

    mean = temp // len(visited)
    for country in visited:
        people[country[0]][country[1]] = mean
    return moved


N,L,R = map(int, sys.stdin.readline().split())
people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


result = 0
while True:
    real_visited = [[0]*N for _ in range(N)]
    temp = False
    for i in range(N):
        for j in range(N):
            if real_visited[i][j] == 0:
                if bfs(i,j):
                    if temp == False:
                        temp = True
    if temp == True:
        result += 1
    else:
        break
print(result)