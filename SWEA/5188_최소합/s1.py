import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == 0 and j > 0: # 맨 윗줄
                numbers[i][j] += numbers[i][j-1]
            elif j == 0 and i > 0: # 맨 왼쪽 줄
                numbers[i][j] += numbers[i-1][j]
            elif i != 0 and j != 0:
                numbers[i][j] += min(numbers[i-1][j], numbers[i][j-1])
    result = numbers[N-1][N-1]
    print("#{} {}".format(tc+1, result))