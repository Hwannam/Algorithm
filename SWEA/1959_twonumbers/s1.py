import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))

    result = 0
    if N <= M:
        for move in range(M - N + 1):
            sum_mul = 0
            for i in range(N):
                sum_mul += ai[i] * bj[i+move]
            result = max(result, sum_mul)
    else:
        for move in range(N - M + 1):
            sum_mul = 0
            for i in range(M):
                sum_mul += ai[i+move] * bj[i]
            result = max(result, sum_mul)
    print("#{} {}".format(tc+1, result))

