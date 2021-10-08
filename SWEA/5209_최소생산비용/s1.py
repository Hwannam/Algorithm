import sys
sys.stdin = open('input.txt')

def dfs(row, temp):
    global result
    if row >= N:
        result = min(result, temp)
        return
    for i in range(N):
        if visited[i] == 0:
            if result <= temp + cost[row][i]:
                continue
            else:
                visited[i] = 1
                temp += cost[row][i]
                dfs(row+1, temp)
                temp -= cost[row][i]
                visited[i] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 1000000
    dfs(0, 0)
    print('#{} {}'.format(tc+1, result))