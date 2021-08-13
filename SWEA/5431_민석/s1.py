import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    not_sub = []
    for num in range(1, N+1):
        if num not in submit:
            not_sub.append(num)

    print("#{}".format(tc + 1), end=" ")
    print(" ".join(map(str, not_sub)))