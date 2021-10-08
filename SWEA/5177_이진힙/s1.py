import sys
sys.stdin = open("input.txt")

def make_heap(i):
    if i > 1:
        if tree[i//2] > tree[i]:
            tree[i], tree[i//2] = tree[i//2], tree[i]
            make_heap(i//2)
    if i+1 <= N:
        make_heap(i+1)

def find_parent(i):
    global answer
    if i >= 1:
        answer += tree[i]
        find_parent(i//2)

T = int(input())
for tc in range(T):
    N = int(input())
    tree = [0]
    tree += list(map(int, input().split()))
    make_heap(1)
    answer = 0
    find_parent(N//2)
    print("#{} {}".format(tc+1, answer))