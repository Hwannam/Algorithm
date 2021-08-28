import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    center = N//2 # 시작 지점
    profit = 0
    distance = N - center - 1 # 시작지점에서 이동할 거리
    for i in range(-distance, distance + 1):
        for j in range(-distance, distance + 1):
            if abs(i) + abs(j) <= distance:
                profit += farm[center+i][center+j]
    print("#{} {}".format(tc+1, profit))