import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))
    corridor = [0 for _ in range(200)]
    for room_num in room:
        room_num.sort()
        start = (room_num[0] - 1) // 2
        end = (room_num[1] - 1) // 2
        for i in range(start, end+1):
            corridor[i] += 1
    print("#{} {}".format(tc + 1, max(corridor)))