import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    bus = []
    for _ in range(N):
        bus.append(list(map(int, input().split())))
    P = int(input())
    stop = []
    for _ in range(P):
        stop.append([int(input()), 0])
    for i in range(N):
        stop_num = bus[i][0]
        while stop_num <= bus[i][1]:
            for j in range(P):
                if stop_num == stop[j][0]:
                    stop[j][1] += 1
            stop_num += 1
    print("#{}".format(tc+1), end = " ")
    for i in range(P):
        print(stop[i][1], end = " ")
    print()