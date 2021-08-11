import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    direction = 0 # 0=우 1=하 2=좌 3=상
    i = j = 0 # 처음 위치

    for num in range(1, N**2 + 1):
        arr[i][j] = num
        
        # 다음으로 가기 전에 미리 테스트 하는 방법
        if i + dy[direction] == N or j + dx[direction] == N\
                or i + dy[direction] == -1 or j + dx[direction] == -1\
                or arr[i + dy[direction]][j + dx[direction]] != 0:  # 다음 진행시 리스트 범위를 벗어나는 경우
                                                                    # 이미 숫자를 갱신한 경우
            direction += 1
            if direction > 3: # 0 1 2 3 다음에 다시 0으로
                direction = 0

        i += dy[direction]
        j += dx[direction]

    print("#{}".format(tc+1))
    for num in arr:
        print(*num)