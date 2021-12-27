N = int(input())
scores = [int(input()) for i in range(N)]
visited = [0 for _ in range(N+1)]

for i in range(1,N+1):
    if i<3:
        visited[i] = visited[i-1] + scores[i-1]
    else:
        visited[i] = max(visited[i-2] + scores[i-1], visited[i-3] + scores[i-2] + scores[i-1])

print(visited[N])