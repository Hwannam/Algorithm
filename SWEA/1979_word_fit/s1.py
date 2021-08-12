import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))
    result = 0

    for i in range(N):
        row_count = col_count = 0
        for j in range(N):
            if puzzle[i][j] == 1: # 각 row에 대하여
                row_count += 1
            else:
                if row_count == K: # 이전까지 1이 K번 반복되었을 경우
                    result += 1
                row_count = 0

            if puzzle[j][i] == 1: # 각 col에 대하여
                col_count += 1
            else:
                if col_count == K: # 이전까지 1이 K번 반복되었을 경우
                    result += 1
                col_count = 0

        if row_count == K: # 마지막 동작의 결과 처리
            result += 1
        if col_count == K:
            result += 1
    print("#{} {}".format(tc+1, result))