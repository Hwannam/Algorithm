import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = []
    stack.append(v)

    while stack:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1
            for w in range(1, V+1):
                if near_list[v][w] == 1 and visited[w] == 0:
                    if w == G:
                        return 1
                    stack.append(w)
    return 0

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    temp = []
    for _ in range(E):
        temp += list(map(int, input().split()))

    S, G = map(int, input().split())
    near_list = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for i in range(0, len(temp) - 1, 2):
        near_list[temp[i]][temp[i + 1]] = 1

    print("#{} {}".format(tc+1, dfs(S)))