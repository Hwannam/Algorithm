import sys
sys.stdin = open('input.txt')

def find_path(S):
    temp = []
    for nodes in info:
        if nodes[0] == S:
            if nodes[1] == G:
                return 1
            else:
                temp.append(nodes)
    for node in temp:
        result = find_path(node[1])
        if result == 1:
            return result
    return 0

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    info = []
    for _ in range(E):
        info.append(list(map(int, input().split())))
    S, G = map(int, input().split())
    print("#{} {}".format(tc+1, find_path(S)))