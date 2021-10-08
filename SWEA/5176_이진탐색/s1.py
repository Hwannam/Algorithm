import sys
sys.stdin = open("input.txt")

def make_tree(i):
    global number
    if i <= N:
        make_tree(i*2)
        tree[i] = number
        number += 1
        make_tree(i*2+1)

T = int(input())
for tc in range(T):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    number = 1
    make_tree(1)
    print("#{} {} {}".format(tc+1, tree[1], tree[int(N/2)]))