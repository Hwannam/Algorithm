import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = []
    stack.append(v)
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            for w in range(100):
                if (arr1[v] == w or arr2[v] == w) and visited[w] == 0:
                    if w == B:
                        return 1
                    stack.append(w)
    return 0

A = 0
B = 99
for _ in range(10):
    arr1 = [-1 for _ in range(100)]
    arr2 = [-1 for _ in range(100)]
    tc, total = map(int, input().split())
    temp = list(map(int, input().split()))

    visited = [0 for _ in range(100)]

    for i in range(0, len(temp) - 1, 2):
        if arr1[temp[i]] == -1:
            arr1[temp[i]] = temp[i+1]
        else:
            arr2[temp[i]] = temp[i+1]
    print("#{} {}".format(tc, dfs(A)))