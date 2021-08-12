import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            count = 0
            for r in range(0, M):
                for c in range(0, M):
                    count += arr[i+r][j+c]
            max_kill = max(max_kill, count)

    print("#{} {}".format(tc+1, max_kill))