import sys
sys.stdin = open("input.txt")

def dfs(row):
    global result
    if row == N:
        result += 1
        return
    for i in range(N):
        if visited[i] == 0:
            if row + i not in left and row - i not in right:
                visited[i] = 1
                left.append(row+i)
                right.append(row-i)
                dfs(row+1)
                visited[i] = 0
                left.pop()
                right.pop()

T = int(input())
for tc in range(T):
    N = int(input())
    left = []
    right = []
    result = 0
    visited = [0]*N
    dfs(0)
    print("#{} {}".format(tc+1, result))