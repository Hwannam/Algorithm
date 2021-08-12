import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    background = [[0]*10 for _ in range(10)]

    for _ in range(N):
        colors = list(map(int, input().split()))

        for i in range(colors[0], colors[2] + 1):
            for j in range(colors[1], colors[3] + 1):
                if background[j][i] != colors[4]:
                    if background[j][i] == 0:
                        background[j][i] = colors[4]
                    else:
                        background[j][i] = 3

    result = 0
    for row in background:
        for square in row:
            if square == 3:
                result += 1
    print("#{} {}".format(tc+1, result))