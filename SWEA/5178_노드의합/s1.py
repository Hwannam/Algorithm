import sys
sys.stdin = open("input.txt")

def make_tree(i):
    if i > 1:
        tree[i//2] = tree[i-1] + tree[i]
        make_tree(i-2)

T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+2)]
    for _ in range(M):
        node_num, number = map(int, input().split())
        tree[node_num] = number
    if N % 2 == 0:
        make_tree(N+1)
    else:
        make_tree(N)
    print("#{} {}".format(tc+1, tree[L]))