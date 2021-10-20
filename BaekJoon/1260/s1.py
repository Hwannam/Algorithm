import sys
from collections import deque

def dfs(V):
    dfs_result.append(V)
    visited[V] = 1
    for i in range(1, N+1):
        if graph[V][i] == 1  and visited[i] == 0:
            dfs(i)
    return

def bfs(V):
    queue = deque()
    queue.append(V)
    visited[V] = 1
    while queue:
        temp = queue.popleft()
        bfs_result.append(temp)
        for i in range(1, N + 1):
            if visited[i] == 0 and graph[temp][i] == 1:
                queue.append(i)
                visited[i] = 1

N, M, V = map(int, sys.stdin.readline().split())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0]*(N+1)
dfs_result = []
bfs_result = []
for number in numbers:
  a, b = number[0], number[1]
  graph[a][b] = graph[b][a] = 1

dfs(V)
visited = [0]*(N+1)
bfs(V)
print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))