import sys
sys.stdin = open('input.txt')

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def find_road(y, x, count):
    while True:
        moved = False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if room[ny][nx] - 1 == room[y][x]:
                    count += 1
                    y = ny
                    x = nx
                    moved = True
                    break
        if not moved:
            return count

T = int(input())
for tc in range(T):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0
    max_room = -1
    for i in range(N):
        for j in range(N):
            temp = find_road(i, j, 1)
            if max_count < temp:
                max_count = temp
                max_room = room[i][j]
            elif max_count == temp:
                max_room = min(max_room, room[i][j])
    print('#{} {} {}'.format(tc+1, max_room, max_count))