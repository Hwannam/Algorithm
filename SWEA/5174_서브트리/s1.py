import sys
sys.stdin = open("input.txt")

def find_subtree(i):
    global answer
    answer += 1
    if tree[0][i] != 0:
        find_subtree(tree[0][i])
    if tree[1][i] != 0:
        find_subtree(tree[1][i])

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    info = list(map(int, input().split()))
    tree = [[0]*(E+2) for _ in range(2)]
    for i in range(0, 2*E, 2):
        if tree[0][info[i]] == 0:
            tree[0][info[i]] = info[i+1]
        else:
            tree[1][info[i]] = info[i+1]
    answer = 0
    find_subtree(N)
    print("#{} {}".format(tc+1, answer))