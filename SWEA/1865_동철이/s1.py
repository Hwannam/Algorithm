import sys
sys.stdin = open('input.txt')

def dfs(row):
    global result, temp
    if row >= N:
        result = max(result, temp*100)
        return
    for i in range(N):
        if visited[i] == 0:
            if result >= temp * numbers[row][i]:
                continue
            else:
                visited[i] = 1
                temp *= (numbers[row][i] / 100)
                dfs(row+1)
                temp /= (numbers[row][i] / 100)
                visited[i] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    temp = 1
    dfs(0)
    print('#{} {:.6f}'.format(tc+1, round(result,6)))