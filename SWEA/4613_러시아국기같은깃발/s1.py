import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    string = [input() for _ in range(N)]
    cover = 0
    for i in range(M):
        if string[0][i] != 'W':
            cover += 1
        if string[N-1][i] != 'R':
            cover += 1

    min_change = N * M
    for i in range(N-2):
        white = 0
        if i != 0:
            for j in range(1, i+1):
                white += (M - string[j].count('W'))

        for j in range(i+1, N-1):
            blue = 0
            for k in range(i+1, j+1):
                blue += (M - string[k].count('B'))
            red = 0
            for k in range(j+1, N-1):
                red +=  (M - string[k].count('R'))
            if white + blue + red < min_change:
                min_change = white + blue + red
    cover += min_change
    print("#{} {}".format(tc+1, cover))