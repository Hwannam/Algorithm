import sys
sys.stdin = open("input.txt")

def find_tree(i):
    global answer
    if i <= N:
        find_tree(i*2)
        answer += tree[i][1]
        find_tree(i*2 + 1)

for tc in range(10):
    N = int(input())
    tree = [list(input().split()) for _ in range(N)]
    for i in range(N):
        tree[i][0] = int(tree[i][0])
    answer = ""
    tree.insert(0, [])

    find_tree(1)
    print("#{} {}".format(tc+1, answer))