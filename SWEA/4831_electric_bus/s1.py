import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    list_M = list(map(int, input().split()))
    location = 0    # 현재 위치
    move = K        # 이동할 거리
    charge = 0      # 충전 횟수
    while True:
        if move == 0:   # 한 번 충전으로 이동가능한 K이내에 충전소가 없는 경우
            charge = 0  # 종점에 도착할 수 없으므로 0을 출력
            break

        if location + move in list_M:  # 현 위치에서 move 만큼 이동했을때 충전소가 있는 곳이면
            location += move           # move 만큼 이동한다.
            charge += 1
            move = K
        elif location + K >= N:        # 현 위치에서 최대 이동거리 만큼 이동했는데 종점 도착시
            break
        else:                          # 이동할 거리는 최대 이동거리 K에서 1씩 감소 시킨다.
            move -= 1

    print("#{} {}".format(tc + 1, charge))