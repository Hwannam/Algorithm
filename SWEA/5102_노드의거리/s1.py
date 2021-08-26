import sys
sys.stdin = open("input.txt")

def bfs(v):
    queue = []
    visited = [0] * (V+1)
    visited[v] = 1
    distance = [0] * (V+1)
    queue.append(v)

    if S == G:
        return 0
    while queue:
        new_v = queue.pop(0)
        for nb in range(1, 1+V):
            if K[new_v][nb] == 1 and visited[nb] == 0:
                queue.append(nb)
                visited[nb] = 1
                distance[nb] = distance[new_v] + 1
                if nb == G:
                    return distance[nb]
    return 0

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    node_num = []
    for _ in range(E):
        node_num += list(map(int, input().split()))
    S, G  = map(int, input().split())

    K = [[0 for i in range(V + 1)] for j in range(V + 1)]

    # 인접행렬
    for i in range(0, len(node_num), 2):
        K[node_num[i]][node_num[i + 1]] = 1
        K[node_num[i + 1]][node_num[i]] = 1
    print("#{} {}".format(tc+1, bfs(S)))