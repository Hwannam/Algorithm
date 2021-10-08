import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    count = 0
    lane, length = map(int, input().split())
    flag = []
    Red = False
    Blue = False
    White = False
    # 국기를 만들때 각각 한줄은 만들고 첫줄은 흰색
    # 마지막줄은 빨간색이니까
    # 첫줄 마지막줄을 먼저칠하고 가장 파랑이 많은곳에 파랑칠하고
    # 그 사이는 파랑-흰색 많은곳 or 파랑-빨간 많은곳

    # 플래그 정의받기
    for _ in range(lane):
        flag.append(list(map(str, input())))
    # 가장 윗줄 흰색칠하기
    for i in range(length):
        if flag[0][i] != 'W':
            flag[0][i] = 'W'
            count += 1
    print(count)

    # 가장 아랫줄 빨간색칠하기
    for j in range(length):
        if flag[lane-1][j] != 'R':
            flag[lane-1][j] = 'R'
            count += 1
    print(count)

    # 파랑색이 가장 많은 찾기
    for