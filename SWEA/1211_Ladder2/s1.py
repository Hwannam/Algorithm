import sys
sys.stdin = open("input.txt")

for _ in range(10):
    tc = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))

    direction = ""  # 방향 유지를 위함
    result = 0
    move_min = 10000
    for x in range(100):
        y = 0
        start = x
        if ladder[y][x] == 1:
            move = 0
            while y < 99:  # 맨 아래에 도착하기 전까지
                left = x - 1
                right = x + 1
                move += 1
                if left >= 0 and ladder[y][left] == 1:  # 맨 왼쪽일때는 left를 체크할 필요가 없다.
                    if direction == "right":  # 이전 방향이 오른쪽이었다면 현재 왼쪽이 1이어도 무시
                        pass
                    else:  # 이전에 오른쪽 이동이 아니었고 왼쪽에 1이 있다면
                        direction = "left"  # 왼쪽 이동으로 바꾸고
                        x -= 1  # 좌표 이동
                        continue  # 다른 코드 무시

                if right <= 99 and ladder[y][right] == 1:  # 맨 오른쪽일때는 right를 체크할 필요가 없다.
                    if direction == "left":  # 이전 방향이 왼쪽이었다면 현재 오른쪽이 1이어도 무시
                        pass
                    else:  # 이전에 왼쪽 이동이 아니었고 오른쪽에 1이 있다면
                        direction = "right"  # 오른쪽 이동으로 바꾸고
                        x += 1  # 좌표 이동
                        continue  # 다른 코드 무시
                y += 1  # 왼쪽 오른쪽이 둘다 0이면 아래로 이동
                direction = ""  # 방향 초기화
            if move <= move_min:
                move_min = move
                result = start
    print("#{} {}".format(tc, result))